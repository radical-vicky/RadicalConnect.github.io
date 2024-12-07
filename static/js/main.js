document.getElementById('searchButton').addEventListener('click', function() {
    var query = document.getElementById('searchInput').value;
    if (query) {
        // Perform the search action, e.g., redirect to a search results page
        window.location.href = 'searchResultsPage.html?query=' + encodeURIComponent(query);
    } else {
        alert('Please enter a search term.');
    }
});
