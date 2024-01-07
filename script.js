function symptomCheck() {
  let symptomForm = document.getElementById("symptom-form");
  let inputs = Array.from(symptomForm.getElementsByTagName("input")).filter((element) => element.type === "checkbox");
  let values = inputs.map((input) => input.checked ? 1 : 0);

  if (values.every(value => value === 0)) {
    alert("Please check at least one symptom");
  } else {
    console.log(JSON.stringify(values));
    fetch('http://127.0.0.1:8001/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(values),
    })
      .then(response => response.json())
      .then(data => {
        console.log('Prediction:', data.prediction);
        displayPredictionResult(data.prediction);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
}

function displayPredictionResult(prediction) {
  let predictionResultElement = document.getElementById("prediction-result");
  predictionResultElement.innerHTML = `Prediction: ${prediction}`;
}
