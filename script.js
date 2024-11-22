// Function to show the Sign-Up form
function showSignUp() {
    document.getElementById("auth-container").classList.add("hidden");
    document.getElementById("signup-container").classList.remove("hidden");
  }
  
  // Function to show the Sign-In form
  function showSignIn() {
    document.getElementById("signup-container").classList.add("hidden");
    document.getElementById("auth-container").classList.remove("hidden");
  }
  
  // Function to handle Sign-Up and show the Interest page
  function handleSignUp(event) {
    event.preventDefault(); // Prevent form submission
    localStorage.setItem("isFirstTimeUser", "true"); // Set first-time flag
    showInterestSelection();
  }
  
  // Function to show Interest Selection page
  function showInterestSelection() {
    document.getElementById("signup-container").classList.add("hidden");
    document.getElementById("interest-container").classList.remove("hidden");
  }
  
  // Function to handle Sign-In and navigate based on user status
  function handleSignIn(event) {
    event.preventDefault(); // Prevent form submission
    const isFirstTimeUser = localStorage.getItem("isFirstTimeUser");
    if (isFirstTimeUser === "true") {
        showInterestSelection();
    } else {
        showVibeSpace();
    }
  }
  
  // Function to save user interests from Interest Selection form
  function handleInterestSelection(event) {
    event.preventDefault(); // Prevent form submission
    const interests = document.getElementById("interest-input").value
        .split(',')
        .map(interest => interest.trim().toLowerCase()); // Convert to lowercase for matching
  
    localStorage.setItem("userInterests", JSON.stringify(interests)); // Save interests in localStorage
    showVibeSpace(); // Show main VibeSpace page after saving interests
  }
  
  // Function to show the VibeSpace main page
  function showVibeSpace() {
    document.getElementById("interest-container").classList.add("hidden");
    document.getElementById("main-container").classList.remove("hidden");
    localStorage.setItem("isFirstTimeUser", "false"); // Clear first-time flag
  }
  
  // Notify user based on their interests when a new room is created
  function notifyUserAboutTopic(roomTopic) {
    const userInterests = JSON.parse(localStorage.getItem("userInterests") || "[]");
  
    if (userInterests.includes(roomTopic.toLowerCase())) {
        alert(Notification: A new room about "${roomTopic}" has been created!);
    }
  }
  
  // Simulate the creation of a new room
  function createRoom() {
    const roomTopic = prompt("Enter a topic for the new room:");
    if (roomTopic) {
        notifyUserAboutTopic(roomTopic.trim());
    }
  }
  
  // Attach event listeners to forms
  document.getElementById("signup-form").addEventListener("submit", handleSignUp);
  document.getElementById("signin-form").addEventListener("submit", handleSignIn);
  document.getElementById("interest-form").addEventListener("submit", handleInterestSelection);
  
  // Add event listeners to the dashboard buttons
  document.getElementById("create-room-btn").addEventListener("click", createRoom);
  document.getElementById("focus-rooms-btn").addEventListener("click", () => {
    alert("Welcome to Focus Rooms!");
  });