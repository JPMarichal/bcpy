document.addEventListener('DOMContentLoaded', function() {
    // Theme switcher
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            document.body.dataset.theme = 
                document.body.dataset.theme === 'dark' ? 'light' : 'dark';
            localStorage.setItem('theme', document.body.dataset.theme);
        });
    }

    // Initialize theme from localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.body.dataset.theme = savedTheme;
    }

    // WYSIWYG Editor initialization for content creation
    const editorElements = document.querySelectorAll('.wysiwyg-editor');
    editorElements.forEach(element => {
        const toolbar = document.createElement('div');
        toolbar.className = 'editor-toolbar';
        toolbar.innerHTML = `
            <button type="button" data-command="bold"><i class="fas fa-bold"></i></button>
            <button type="button" data-command="italic"><i class="fas fa-italic"></i></button>
            <button type="button" data-command="createLink"><i class="fas fa-link"></i></button>
        `;
        
        element.parentNode.insertBefore(toolbar, element);
        
        toolbar.querySelectorAll('button').forEach(button => {
            button.addEventListener('click', () => {
                const command = button.dataset.command;
                if (command === 'createLink') {
                    const url = prompt('Enter URL:');
                    if (url) document.execCommand(command, false, url);
                } else {
                    document.execCommand(command, false, null);
                }
            });
        });
    });

    // Search functionality
    const searchForm = document.getElementById('search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const query = document.getElementById('search-input').value;
            try {
                const response = await fetch(`/search?q=${encodeURIComponent(query)}`);
                const results = await response.json();
                displaySearchResults(results);
            } catch (error) {
                console.error('Search error:', error);
            }
        });
    }
});

function displaySearchResults(results) {
    const resultsContainer = document.getElementById('search-results');
    if (!resultsContainer) return;

    resultsContainer.innerHTML = results.map(result => `
        <div class="search-result">
            <h3><a href="${result.url}">${result.title}</a></h3>
            <p>${result.excerpt}</p>
        </div>
    `).join('');
}
