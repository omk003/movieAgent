document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.getElementById('send-button');
    const userInput = document.getElementById('user-input');

    sendButton.addEventListener('click', function() {
        const userMessage = userInput.value;
        if (userMessage.trim() !== "") {
            fetch('/send-message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userMessage })
            })
            .then(response => response.json())
            .then(data => {
                displayMessage('User', userMessage);
                displayMessage('Bot', data.reply);
            })
            .catch(error => console.error('Error:', error));

            userInput.value = ''; // Clear the input after sending
        }
    });

    function displayMessage(sender, message) {
        const chatBox = document.getElementById('chat-box');
        const messageDiv = document.createElement('div');
        messageDiv.className = sender.toLowerCase() + '-message';
        messageDiv.textContent = message;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});
