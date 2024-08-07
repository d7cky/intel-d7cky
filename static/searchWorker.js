self.onmessage = function(event) {
    const { originalContent, searchTerm } = event.data;
    const regex = new RegExp(searchTerm, 'gi');
    let match;
    let lastIndex = 0;
    let highlightedContent = '';
    const highlights = [];

    while ((match = regex.exec(originalContent)) !== null) {
        highlights.push(match.index);
        highlightedContent += escapeHtml(originalContent.slice(lastIndex, match.index));
        highlightedContent += `<mark class="highlight">${escapeHtml(match[0])}</mark>`;
        lastIndex = regex.lastIndex;
    }
    highlightedContent += escapeHtml(originalContent.slice(lastIndex));

    self.postMessage({ highlightedContent, highlights });
};

function escapeHtml(unsafe) {
    return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}