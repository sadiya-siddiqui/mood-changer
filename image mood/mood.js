
const images = [
  { id: "happy_image", mood: "Happy" },
  { id: "sad_image", mood: "Sad" },
  { id: "anger_image", mood: "Angry" },
  { id: "suspense_image", mood: "Suspense" }
];

let currentIndex = 0;

function updateMood() {
  // Hide all images
  images.forEach(img => {
    document.getElementById(img.id).style.display = "none";
  });

  // Show current image
  const currentImage = images[currentIndex];
  document.getElementById(currentImage.id).style.display = "block";

  // Update mood text
  document.getElementById("moodText").innerText = `Mood: ${currentImage.mood}`;

  // Move to next mood index
  currentIndex = (currentIndex + 1) % images.length;
}

document.getElementById("changeMoodButton").addEventListener("click", updateMood);

// Optional: Show the first image by default
updateMood();