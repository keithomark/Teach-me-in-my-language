async function generateExplanation() {
    const topic = document.getElementById('topic').value.trim();
    const language = document.getElementById('language').value;
    const outputSection = document.getElementById('outputSection');
    const outputContent = document.getElementById('outputContent');

    if (!topic) {
        alert('Please enter a topic to learn about!');
        return;
    }

    // Show loading state
    outputSection.style.display = 'block';
    outputContent.innerHTML = '<div class="loading">Generating your desi explanation... 🚀</div>';

    try {
        // First, get the explanation
        const explainResponse = await fetch('/api/explain', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ topic })
        });

        if (!explainResponse.ok) {
            throw new Error('Failed to generate explanation');
        }

        const { explanation } = await explainResponse.json();

        // Then, translate it
        const translateResponse = await fetch('/api/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: explanation,
                target_lang: language
            })
        });

        if (!translateResponse.ok) {
            throw new Error('Failed to translate explanation');
        }

        const { translated_text } = await translateResponse.json();

        // Display the result
        outputContent.innerHTML = `
            <div class="explanation">
                <h3>Here's your topic in ${language.charAt(0).toUpperCase() + language.slice(1)}:</h3>
                <p>${translated_text}</p>
            </div>
        `;
    } catch (error) {
        console.error('Error:', error);
        outputContent.innerHTML = `
            <div class="error">
                Oops! Something went wrong. Please try again later. 🙏
            </div>
        `;
    }
}

function createConfetti() {
    const confettiCount = 50;
    const container = document.querySelector('.container');
    
    for (let i = 0; i < confettiCount; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = Math.random() * 100 + 'vw';
        confetti.style.animationDelay = Math.random() * 3 + 's';
        confetti.innerHTML = ['🚀', '💡', '📚', '✨', '🎓'][Math.floor(Math.random() * 5)];
        container.appendChild(confetti);
        
        // Remove confetti after animation
        setTimeout(() => {
            confetti.remove();
        }, 3000);
    }
} 