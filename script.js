function encryptMessage() {
    const message = document.getElementById('message').value;
    const key = parseInt(document.getElementById('key').value);
    if (!message || isNaN(key) || key < 1 || key > 25) {
        alert('Please enter a valid message and a key between 1 and 25.');
        return;
    }

    const encryptedMessage = caesarCipher(message, key);
    displayOutput(`Encrypted Message: ${encryptedMessage}`);
}

function decryptMessage() {
    const message = document.getElementById('message').value;
    const key = parseInt(document.getElementById('key').value);
    if (!message || isNaN(key) || key < 1 || key > 25) {
        alert('Please enter a valid message and a key between 1 and 25.');
        return;
    }

    const decryptedMessage = caesarCipher(message, -key);
    displayOutput(`Decrypted Message: ${decryptedMessage}`);
}

function caesarCipher(str, key) {
    return str.split('').map(char => {
        if (char.match(/[a-z]/i)) {
            const code = char.charCodeAt(0);
            const base = code >= 65 && code <= 90 ? 65 : 97;
            return String.fromCharCode(((code - base + key + 26) % 26) + base);
        }
        return char;
    }).join('');
}

function displayOutput(result) {
    const output = document.getElementById('output');
    output.style.display = 'block';
    output.textContent = result;
}
