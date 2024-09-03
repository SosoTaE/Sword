const NOT_FOUND_IMAGE_PATH = '../static/assets/sad.png'
const NOT_FOUND_MESSAGE = "ბოდიში, შედეგები ვერ მოიძებნა"


document.getElementById("modalButton").addEventListener("click", function () {
  let element = document.getElementById("modal");
  element.style.display = "none";
});

const notFoundMessage = document.getElementById("notFound")
const searchButton = document.getElementById("searchButton")

function addNotFoundMessage(element) {
      const div = document.createElement("div")
      div.id = "notFound"
      div.classList.add("no__res")
      div.style.display = "flex"

      const img = document.createElement("img")
      img.src = NOT_FOUND_IMAGE_PATH

      const p = document.createElement("p")
      p.innerHTML = NOT_FOUND_MESSAGE

      div.appendChild(img)
      div.appendChild(p)

      element.appendChild(div)

  }

function addWords(words, results) {
        results.innerHTML = ""
        for (let i = 0;i < words.length;i++) {
            const p = document.createElement("p")
            p.classList.add("res__item")

            const wordSpan = document.createElement("span")
            wordSpan.innerHTML = words[i].word
            wordSpan.style.backgroundColor = `rgb(0,${255 * words[i].similarity},0)`

              const similaritySpan = document.createElement("span")
            similaritySpan.innerHTML = words[i].similarity
              similaritySpan.style.backgroundColor = `rgb(0,${255 * words[i].similarity},0)`
            p.appendChild(wordSpan)
            p.innerHTML += "-"
            p.appendChild(similaritySpan)
              results.appendChild(p)
        }
  }

searchButton.addEventListener("click", async () => {
  const promptInput = document.getElementById("promptInput").value
  const similarityLevel = document.getElementById("similarityLevel").value

  const requestBody = {
    "word": promptInput.trim(),
    "minimum_similarity": Number(similarityLevel)
  }

  await fetch(`${location.origin}/similarWords`, {
    method: "POST",
    body: JSON.stringify(requestBody),
    headers: {
    "Content-Type": "application/json"
    },
  })
      .then(data => data.json())
      .then(data => {
        const results = document.getElementById("results")
        results.innerHTML = ""
        const words = data["words"].sort((a,b) => {
            return b.similarity - a.similarity
        })
        if (words.length == 0) {
            addNotFoundMessage(results)
        }
        else {
           addWords(words,results)
        }
      })

})
