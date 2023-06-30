document.addEventListener('DOMContentLoaded', function() {
  const postBlock = document.getElementById('postBlock');
  const postText = document.getElementById('postText');
  const yesButton = document.getElementById('yesButton');
  const noButton = document.getElementById('noButton');
  
  yesButton.addEventListener('click', function() {
    const text = postText.textContent;
    fetch('/post', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text })
    })
      .then(response => {
        if (response.ok) {
          postText.textContent = "The post has been successfully sent to the channel."
        } else {
          throw new Error('Request failed');
        }
      })
      .catch(error => console.error(error));
  });

  noButton.addEventListener('click', function() {
    postText.textContent = "Post creating, please wait...";
    fetch('/create')
      .then(response => response.json())
      .then(data => {
        postText.textContent = data.text;
        postText.style.whiteSpace = "pre-line";
        yesButton.style.display = "block";
      })
      .catch(error => console.error(error));
  });
});
