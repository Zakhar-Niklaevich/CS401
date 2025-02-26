document.getElementById("recommendForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let inputSong = document.getElementById("songs").value.trim();
    
    if (!inputSong) return;

    fetch("/api/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ "songs": [inputSong] })
    })
    .then(response => response.json())
    .then(data => {
        let resultsContainer = document.getElementById("results-container");
        resultsContainer.style.display = "block"; // Show results section

        let yourSongList = document.getElementById("your-song");
        yourSongList.innerHTML = "";
        let yourSongItem = createSongElement(inputSong);
        yourSongList.appendChild(yourSongItem);

        let recommendationsList = document.getElementById("recommendations");
        recommendationsList.innerHTML = "";
        data.songs.forEach(song => {
            let li = createSongElement(song);
            recommendationsList.appendChild(li);
        });
    })
    .catch(error => console.error("Error fetching recommendations:", error));
});

// Function to create song list item with play button
function createSongElement(songName) {
    let li = document.createElement("li");
    li.textContent = songName;

    let playButton = document.createElement("button");
    playButton.className = "play-button";
    playButton.innerHTML = "▶";
    playButton.onclick = () => openYouTube(songName);

    li.appendChild(playButton);
    return li;
}

// Function to open YouTube search or first video
function openYouTube(songName) {
    let query = encodeURIComponent(songName + " song");
    
    // Try to fetch first video result (if CORS allows)
    fetch(`https://www.youtube.com/results?search_query=${query}`, { mode: 'no-cors' })
    .then(() => {
        window.open(`https://www.youtube.com/results?search_query=${query}`, "_blank");
    })
    .catch(() => {
        // If fetch fails, open YouTube search page instead
        window.open(`https://www.youtube.com/results?search_query=${query}`, "_blank");
    });
}
