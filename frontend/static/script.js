document.getElementById("recommendForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let inputSongs = document.getElementById("songs").value.split(",").map(s => s.trim());
    
    fetch("/api/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ "songs": inputSongs })
    })
    .then(response => response.json())
    .then(data => {
        let recommendationsList = document.getElementById("recommendations");
        recommendationsList.innerHTML = "";
        data.songs.forEach(song => {
            let li = document.createElement("li");
            li.textContent = song;
            recommendationsList.appendChild(li);
        });
    })
    .catch(error => console.error("Error fetching recommendations:", error));
});
