const stripe = Stripe("pk_test_51KyyMtEUSVW7Sz1sy5Jl5Lu3V8WargxHJh4yfUGKupPIRwZ7oxurpMWedQ9z1SXipvxMTdKk5U2CxnXVVQ2cV05S00WBkcxrrj");



let elements;
let orderNumber;

initialize();
checkStatus();

document
  .querySelector("#payment-form")
  .addEventListener("submit", handleSubmit);

// Fetches a payment intent and captures the client secret
async function initialize() {
  const response = await fetch("create-payment-intent", {
    method: "POST",
    headers: { "Content-Type": "application/json" }
  });
  const { clientSecret, order_number } = await response.json();
  orderNumber = order_number

  const appearance = {
    theme: 'night',
    labels: 'floating',
    variables: {
      colorPrimary: '#ffffff',
      colorBackground: '#000000',
      colorDanger: '#ff5858',
      colorDangerText: '#ff5858'
    },
  };
  elements = stripe.elements({ appearance, clientSecret });

  const paymentElement = elements.create("payment");
  paymentElement.mount("#payment-element");
}

async function handleSubmit(e) {
  e.preventDefault();
  setLoading(true);

  const { error } = await stripe.confirmPayment({
    elements,
    confirmParams: {
      // Make sure to change this to your payment completion page
      // return_url: "https://checkmalt.herokuapp.com/checkout/confirmation/" + orderNumber, //uncomment this line in production
      return_url: "http://127.0.0.1:8000/checkout/confirmation/" + orderNumber, // comment this line in production
    },
  });

  // This point will only be reached if there is an immediate error when
  // confirming the payment. Otherwise, your customer will be redirected to
  // your `return_url`. For some payment methods like iDEAL, your customer will
  // be redirected to an intermediate site first to authorize the payment, then
  // redirected to the `return_url`.
  if (error.type === "card_error" || error.type === "validation_error") {
    showMessage(error.message);
  } else {
    showMessage("An unexpected error occured.");
  }

  setLoading(false);
}

// Fetches the payment intent status after payment submission
async function checkStatus() {
  const clientSecret = new URLSearchParams(window.location.search).get(
    "payment_intent_client_secret"
  );

  if (!clientSecret) {
    return;
  }

  const { paymentIntent } = await stripe.retrievePaymentIntent(clientSecret);

  switch (paymentIntent.status) {
    case "succeeded":
      showMessage("Payment succeeded!");
      break;
    case "processing":
      showMessage("Your payment is processing.");
      break;
    case "requires_payment_method":
      showMessage("Your payment was not successful, please try again.");
      break;
    default:
      showMessage("Something went wrong.");
      break;
  }
}

// ------- UI helpers -------

function showMessage(messageText) {
  const messageContainer = document.querySelector("#payment-message");

  messageContainer.classList.remove("hidden");
  messageContainer.classList.add("text-red-700")
  messageContainer.textContent = messageText;

}

// Show a spinner on payment submission
function setLoading(isLoading) {
  if (isLoading) { 
    // Disable the button and show a spinner
    document.querySelector("#submitPayment").disabled = true;
    document.querySelector("#submitPaymentMobile").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    document.querySelector("#spinnerMobile").classList.remove("hidden");
    document.querySelector("#button-text").classList.add("hidden");
    document.querySelector("#button-text-mobile").classList.add("hidden");
  } else {
    document.querySelector("#submitPayment").disabled = false;
    document.querySelector("#submitPaymentMobile").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#spinnerMobile").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
    document.querySelector("#button-text-mobile").classList.add("hidden");
  }
}