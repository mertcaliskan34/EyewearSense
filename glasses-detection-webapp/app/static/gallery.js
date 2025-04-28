document.addEventListener("DOMContentLoaded", function () {
  // Create gallery container if it doesn't exist
  if (!document.getElementById("gallery-container")) {
    const mainContainer = document.querySelector(".container");
    const gallerySection = document.createElement("div");
    gallerySection.className = "gallery-section";
    gallerySection.innerHTML = `
            <div class="gallery-header">
                <h2>Recently Analyzed Images</h2>
                <button id="clear-gallery" class="clear-gallery-btn">
                    <i class="fas fa-trash-alt"></i> Clear All
                </button>
            </div>
            <div id="gallery-container" class="gallery-container"></div>
        `;

    // Insert gallery after result section or at the end of main container
    const resultSection = document.querySelector(".result-section");
    if (resultSection) {
      resultSection.after(gallerySection);
    } else {
      mainContainer.appendChild(gallerySection);
    }

    // Initialize gallery
    initGallery();
  }

  // Initialize gallery with saved images
  function initGallery() {
    const galleryContainer = document.getElementById("gallery-container");
    const savedImages = JSON.parse(
      localStorage.getItem("analyzedImages") || "[]"
    );

    if (savedImages.length === 0) {
      galleryContainer.innerHTML =
        '<p class="no-images">No images analyzed yet</p>';
      return;
    }

    // Clear gallery container
    galleryContainer.innerHTML = "";

    // Add each image to gallery
    savedImages.forEach((item, index) => {
      const galleryItem = document.createElement("div");
      galleryItem.className = "gallery-item";
      galleryItem.innerHTML = `
                <div class="gallery-image">
                    <img src="${item.imageSrc}" alt="Analyzed image ${
        index + 1
      }">
                </div>
                <div class="gallery-info">
                    <p class="${item.resultClass}">
                        ${item.result}
                    </p>
                    <span class="gallery-date">${item.date}</span>
                </div>
                <button class="remove-item" data-index="${index}">
                    <i class="fas fa-times"></i>
                </button>
            `;
      galleryContainer.appendChild(galleryItem);

      // Add animation
      setTimeout(() => {
        galleryItem.classList.add("show");
      }, index * 100);
    });

    // Add event listeners for removing individual items
    document.querySelectorAll(".remove-item").forEach((button) => {
      button.addEventListener("click", function () {
        const index = parseInt(this.getAttribute("data-index"));
        removeGalleryItem(index);
      });
    });

    // Add event listener for clearing all items
    document
      .getElementById("clear-gallery")
      .addEventListener("click", clearGallery);
  }

  // Save current result to gallery
  function saveToGallery() {
    const resultText = document.querySelector(".result-text");
    const resultImage = document.querySelector(".image-container img");

    if (resultText && resultImage) {
      const savedImages = JSON.parse(
        localStorage.getItem("analyzedImages") || "[]"
      );
      const currentImageSrc = resultImage.src;
      const currentResult = resultText.textContent.trim();

      // Generate a unique identifier for this image based on timestamp
      const imageId = new Date().getTime();

      // Get proper CSS class based on result text
      const resultClass = currentResult.includes("Not Detected")
        ? "glasses-not-detected" // Assign red class if "Not Detected" is present
        : "glasses-detected"; // Otherwise, assume it's detected and assign green class

      // Add new item to beginning of array
      savedImages.unshift({
        id: imageId,
        imageSrc: currentImageSrc,
        result: currentResult,
        resultClass: resultClass,
        date: new Date().toLocaleString(),
      });

      // Limit gallery to 10 items
      if (savedImages.length > 10) {
        savedImages.pop(); // Remove oldest item
      }

      localStorage.setItem("analyzedImages", JSON.stringify(savedImages));
      initGallery();
    }
  }

  // Remove item from gallery
  function removeGalleryItem(index) {
    const savedImages = JSON.parse(
      localStorage.getItem("analyzedImages") || "[]"
    );
    const galleryItems = document.querySelectorAll(".gallery-item");

    // Add fade-out animation
    galleryItems[index].classList.add("fade-out");

    setTimeout(() => {
      // Remove from array
      savedImages.splice(index, 1);
      localStorage.setItem("analyzedImages", JSON.stringify(savedImages));

      // Reinitialize gallery
      initGallery();
    }, 300);
  }

  // Clear all gallery items
  function clearGallery() {
    const galleryItems = document.querySelectorAll(".gallery-item");

    // Add fade-out animation to all items
    galleryItems.forEach((item, index) => {
      setTimeout(() => {
        item.classList.add("fade-out");
      }, index * 50);
    });

    setTimeout(() => {
      localStorage.removeItem("analyzedImages");
      initGallery();
    }, galleryItems.length * 50 + 300);
  }

  // Check if there's a result and save it to gallery
  const resultSection = document.querySelector(".result-section");
  if (resultSection) {
    saveToGallery();
  }

  // Add gallery styles if not already added
  if (!document.getElementById("gallery-styles")) {
    const styleElement = document.createElement("style");
    styleElement.id = "gallery-styles";
    styleElement.textContent = `
            .gallery-section {
                margin-top: 2rem;
                animation: cardAppear 0.5s ease-out;
            }
            
            .gallery-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1rem;
            }
            
            .gallery-header h2 {
                color: var(--text-color);
                font-size: 1.5rem;
                margin: 0;
            }
            
            .clear-gallery-btn {
                background-color: var(--delete-color);
                color: white;
                border: none;
                border-radius: 4px;
                padding: 0.5rem 1rem;
                cursor: pointer;
                display: flex;
                align-items: center;
                gap: 0.5rem;
                transition: all 0.3s ease;
            }
            
            .clear-gallery-btn:hover {
                background-color: var(--delete-hover);
                transform: translateY(-2px);
            }
            
            .gallery-container {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
                gap: 1rem;
                margin-top: 1rem;
            }
            
            .gallery-item {
                background-color: var(--card-bg);
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 4px 8px var(--card-shadow);
                transition: all 0.3s ease;
                position: relative;
                opacity: 0;
                transform: translateY(20px);
            }
            
            .gallery-item.show {
                opacity: 1;
                transform: translateY(0);
            }
            
            .gallery-item:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 16px var(--card-shadow);
            }
            
            .gallery-image {
                height: 150px;
                overflow: hidden;
            }
            
            .gallery-image img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                transition: transform 0.3s ease;
            }
            
            .gallery-item:hover .gallery-image img {
                transform: scale(1.1);
            }
            
            .gallery-info {
                padding: 0.75rem;
            }
            
            .gallery-info p {
                margin: 0 0 0.5rem 0;
                font-size: 0.9rem;
                font-weight: bold;
            }
            
            .gallery-date {
                font-size: 0.8rem;
                color: var(--footer-color);
            }
            
            .remove-item {
                position: absolute;
                top: 5px;
                right: 5px;
                background-color: var(--delete-color);
                color: white;
                border: none;
                border-radius: 50%;
                width: 24px;
                height: 24px;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                opacity: 0.7;
                transition: all 0.3s ease;
            }
            
            .remove-item:hover {
                opacity: 1;
                transform: rotate(90deg);
            }
            
            .no-images {
                grid-column: 1 / -1;
                text-align: center;
                padding: 2rem;
                color: var(--footer-color);
                font-style: italic;
                background-color: var(--card-bg);
                border-radius: 8px;
                box-shadow: 0 4px 8px var(--card-shadow);
            }
            
            @media (max-width: 768px) {
                .gallery-container {
                    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
                }
                
                .gallery-header {
                    flex-direction: column;
                    align-items: flex-start;
                    gap: 0.5rem;
                }
                
                .clear-gallery-btn {
                    font-size: 0.9rem;
                    padding: 0.4rem 0.8rem;
                }
            }
        `;
    document.head.appendChild(styleElement);
  }
});
