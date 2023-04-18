// Replace the below URL with the API endpoint for getting live counts
const API_URL = 'https://socialcounts.org/compare/youtube-live-subscriber-count/UC8Am29Ya-UUSjgwg8Vz-sgA/youtube-live-subscriber-count/UCcBNWxvAXH-nTAzOeuuLHgw/embed';

// Get the count element
const countElement = document.getElementById('count');

// Fetch the live counts from the API
fetch(API_URL)
  .then(response => response.json())
  .then(data => {
    // Update the count element with the live counts
    countElement.textContent = data.count;
  })
  .catch(error => {
    console.error('Error fetching live counts:', error);
  });
