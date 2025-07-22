async function fetchThreats() {
    try {
        const response = await fetch('/fetch-threats');
        const result = await response.json();
        alert(`Success: ${result.message}`);
        location.reload();
    } catch (error) {
        alert('Error fetching threats');
    }
}

async function calculateRisks() {
    try {
        const response = await fetch('/calculate-risks', { method: 'POST' });
        const result = await response.json();
        alert(`Success: ${result.message}`);
        location.reload();
    } catch (error) {
        alert('Error calculating risks');
    }
}