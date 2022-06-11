/******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
/*!***********************************************!*\
  !*** ./checkout/static/js/stripe_elements.js ***!
  \***********************************************/
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
      //return_url: "https://checkmalt.herokuapp.com/checkout/confirmation/" + orderNumber, //uncomment this line in production
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
/******/ })()
;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZGlzdC9zdHJpcGUuYnVuZGxlLmpzIiwibWFwcGluZ3MiOiI7Ozs7O0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsZUFBZTtBQUNmLEdBQUc7QUFDSCxVQUFVLDZCQUE2QjtBQUN2QztBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEtBQUs7QUFDTDtBQUNBLCtCQUErQiwwQkFBMEI7QUFDekQ7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsVUFBVSxRQUFRO0FBQ2xCO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxLQUFLO0FBQ0wsR0FBRztBQUNIO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxJQUFJO0FBQ0o7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxVQUFVLGdCQUFnQjtBQUMxQjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsQyIsInNvdXJjZXMiOlsid2VicGFjazovL2NoZWNrbWFsdHMvLi9jaGVja291dC9zdGF0aWMvanMvc3RyaXBlX2VsZW1lbnRzLmpzIl0sInNvdXJjZXNDb250ZW50IjpbImNvbnN0IHN0cmlwZSA9IFN0cmlwZShcInBrX3Rlc3RfNTFLeXlNdEVVU1ZXN1N6MXN5NUpsNUx1M1Y4V2FyZ3hISmg0eWZVR0t1cFBJUndaN294dXJwTVdlZFE5ejFTWGlwdnhNVGRLazVVMkN4blhWVlEyY1YwNVMwMFdCa2N4cnJqXCIpO1xyXG5cclxuXHJcblxyXG5sZXQgZWxlbWVudHM7XHJcbmxldCBvcmRlck51bWJlcjtcclxuXHJcbmluaXRpYWxpemUoKTtcclxuY2hlY2tTdGF0dXMoKTtcclxuXHJcbmRvY3VtZW50XHJcbiAgLnF1ZXJ5U2VsZWN0b3IoXCIjcGF5bWVudC1mb3JtXCIpXHJcbiAgLmFkZEV2ZW50TGlzdGVuZXIoXCJzdWJtaXRcIiwgaGFuZGxlU3VibWl0KTtcclxuXHJcbi8vIEZldGNoZXMgYSBwYXltZW50IGludGVudCBhbmQgY2FwdHVyZXMgdGhlIGNsaWVudCBzZWNyZXRcclxuYXN5bmMgZnVuY3Rpb24gaW5pdGlhbGl6ZSgpIHtcclxuICBjb25zdCByZXNwb25zZSA9IGF3YWl0IGZldGNoKFwiY3JlYXRlLXBheW1lbnQtaW50ZW50XCIsIHtcclxuICAgIG1ldGhvZDogXCJQT1NUXCIsXHJcbiAgICBoZWFkZXJzOiB7IFwiQ29udGVudC1UeXBlXCI6IFwiYXBwbGljYXRpb24vanNvblwiIH1cclxuICB9KTtcclxuICBjb25zdCB7IGNsaWVudFNlY3JldCwgb3JkZXJfbnVtYmVyIH0gPSBhd2FpdCByZXNwb25zZS5qc29uKCk7XHJcbiAgb3JkZXJOdW1iZXIgPSBvcmRlcl9udW1iZXJcclxuXHJcbiAgY29uc3QgYXBwZWFyYW5jZSA9IHtcclxuICAgIHRoZW1lOiAnbmlnaHQnLFxyXG4gICAgbGFiZWxzOiAnZmxvYXRpbmcnLFxyXG4gICAgdmFyaWFibGVzOiB7XHJcbiAgICAgIGNvbG9yUHJpbWFyeTogJyNmZmZmZmYnLFxyXG4gICAgICBjb2xvckJhY2tncm91bmQ6ICcjMDAwMDAwJyxcclxuICAgICAgY29sb3JEYW5nZXI6ICcjZmY1ODU4JyxcclxuICAgICAgY29sb3JEYW5nZXJUZXh0OiAnI2ZmNTg1OCdcclxuICAgIH0sXHJcbiAgfTtcclxuICBlbGVtZW50cyA9IHN0cmlwZS5lbGVtZW50cyh7IGFwcGVhcmFuY2UsIGNsaWVudFNlY3JldCB9KTtcclxuXHJcbiAgY29uc3QgcGF5bWVudEVsZW1lbnQgPSBlbGVtZW50cy5jcmVhdGUoXCJwYXltZW50XCIpO1xyXG4gIHBheW1lbnRFbGVtZW50Lm1vdW50KFwiI3BheW1lbnQtZWxlbWVudFwiKTtcclxufVxyXG5cclxuYXN5bmMgZnVuY3Rpb24gaGFuZGxlU3VibWl0KGUpIHtcclxuICBlLnByZXZlbnREZWZhdWx0KCk7XHJcbiAgc2V0TG9hZGluZyh0cnVlKTtcclxuXHJcbiAgY29uc3QgeyBlcnJvciB9ID0gYXdhaXQgc3RyaXBlLmNvbmZpcm1QYXltZW50KHtcclxuICAgIGVsZW1lbnRzLFxyXG4gICAgY29uZmlybVBhcmFtczoge1xyXG4gICAgICAvLyBNYWtlIHN1cmUgdG8gY2hhbmdlIHRoaXMgdG8geW91ciBwYXltZW50IGNvbXBsZXRpb24gcGFnZVxyXG4gICAgICAvL3JldHVybl91cmw6IFwiaHR0cHM6Ly9jaGVja21hbHQuaGVyb2t1YXBwLmNvbS9jaGVja291dC9jb25maXJtYXRpb24vXCIgKyBvcmRlck51bWJlciwgLy91bmNvbW1lbnQgdGhpcyBsaW5lIGluIHByb2R1Y3Rpb25cclxuICAgICAgcmV0dXJuX3VybDogXCJodHRwOi8vMTI3LjAuMC4xOjgwMDAvY2hlY2tvdXQvY29uZmlybWF0aW9uL1wiICsgb3JkZXJOdW1iZXIsIC8vIGNvbW1lbnQgdGhpcyBsaW5lIGluIHByb2R1Y3Rpb25cclxuICAgIH0sXHJcbiAgfSk7XHJcblxyXG4gIC8vIFRoaXMgcG9pbnQgd2lsbCBvbmx5IGJlIHJlYWNoZWQgaWYgdGhlcmUgaXMgYW4gaW1tZWRpYXRlIGVycm9yIHdoZW5cclxuICAvLyBjb25maXJtaW5nIHRoZSBwYXltZW50LiBPdGhlcndpc2UsIHlvdXIgY3VzdG9tZXIgd2lsbCBiZSByZWRpcmVjdGVkIHRvXHJcbiAgLy8geW91ciBgcmV0dXJuX3VybGAuIEZvciBzb21lIHBheW1lbnQgbWV0aG9kcyBsaWtlIGlERUFMLCB5b3VyIGN1c3RvbWVyIHdpbGxcclxuICAvLyBiZSByZWRpcmVjdGVkIHRvIGFuIGludGVybWVkaWF0ZSBzaXRlIGZpcnN0IHRvIGF1dGhvcml6ZSB0aGUgcGF5bWVudCwgdGhlblxyXG4gIC8vIHJlZGlyZWN0ZWQgdG8gdGhlIGByZXR1cm5fdXJsYC5cclxuICBpZiAoZXJyb3IudHlwZSA9PT0gXCJjYXJkX2Vycm9yXCIgfHwgZXJyb3IudHlwZSA9PT0gXCJ2YWxpZGF0aW9uX2Vycm9yXCIpIHtcclxuICAgIHNob3dNZXNzYWdlKGVycm9yLm1lc3NhZ2UpO1xyXG4gIH0gZWxzZSB7XHJcbiAgICBzaG93TWVzc2FnZShcIkFuIHVuZXhwZWN0ZWQgZXJyb3Igb2NjdXJlZC5cIik7XHJcbiAgfVxyXG5cclxuICBzZXRMb2FkaW5nKGZhbHNlKTtcclxufVxyXG5cclxuLy8gRmV0Y2hlcyB0aGUgcGF5bWVudCBpbnRlbnQgc3RhdHVzIGFmdGVyIHBheW1lbnQgc3VibWlzc2lvblxyXG5hc3luYyBmdW5jdGlvbiBjaGVja1N0YXR1cygpIHtcclxuICBjb25zdCBjbGllbnRTZWNyZXQgPSBuZXcgVVJMU2VhcmNoUGFyYW1zKHdpbmRvdy5sb2NhdGlvbi5zZWFyY2gpLmdldChcclxuICAgIFwicGF5bWVudF9pbnRlbnRfY2xpZW50X3NlY3JldFwiXHJcbiAgKTtcclxuXHJcbiAgaWYgKCFjbGllbnRTZWNyZXQpIHtcclxuICAgIHJldHVybjtcclxuICB9XHJcblxyXG4gIGNvbnN0IHsgcGF5bWVudEludGVudCB9ID0gYXdhaXQgc3RyaXBlLnJldHJpZXZlUGF5bWVudEludGVudChjbGllbnRTZWNyZXQpO1xyXG5cclxuICBzd2l0Y2ggKHBheW1lbnRJbnRlbnQuc3RhdHVzKSB7XHJcbiAgICBjYXNlIFwic3VjY2VlZGVkXCI6XHJcbiAgICAgIHNob3dNZXNzYWdlKFwiUGF5bWVudCBzdWNjZWVkZWQhXCIpO1xyXG4gICAgICBicmVhaztcclxuICAgIGNhc2UgXCJwcm9jZXNzaW5nXCI6XHJcbiAgICAgIHNob3dNZXNzYWdlKFwiWW91ciBwYXltZW50IGlzIHByb2Nlc3NpbmcuXCIpO1xyXG4gICAgICBicmVhaztcclxuICAgIGNhc2UgXCJyZXF1aXJlc19wYXltZW50X21ldGhvZFwiOlxyXG4gICAgICBzaG93TWVzc2FnZShcIllvdXIgcGF5bWVudCB3YXMgbm90IHN1Y2Nlc3NmdWwsIHBsZWFzZSB0cnkgYWdhaW4uXCIpO1xyXG4gICAgICBicmVhaztcclxuICAgIGRlZmF1bHQ6XHJcbiAgICAgIHNob3dNZXNzYWdlKFwiU29tZXRoaW5nIHdlbnQgd3JvbmcuXCIpO1xyXG4gICAgICBicmVhaztcclxuICB9XHJcbn1cclxuXHJcbi8vIC0tLS0tLS0gVUkgaGVscGVycyAtLS0tLS0tXHJcblxyXG5mdW5jdGlvbiBzaG93TWVzc2FnZShtZXNzYWdlVGV4dCkge1xyXG4gIGNvbnN0IG1lc3NhZ2VDb250YWluZXIgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI3BheW1lbnQtbWVzc2FnZVwiKTtcclxuXHJcbiAgbWVzc2FnZUNvbnRhaW5lci5jbGFzc0xpc3QucmVtb3ZlKFwiaGlkZGVuXCIpO1xyXG4gIG1lc3NhZ2VDb250YWluZXIuY2xhc3NMaXN0LmFkZChcInRleHQtcmVkLTcwMFwiKVxyXG4gIG1lc3NhZ2VDb250YWluZXIudGV4dENvbnRlbnQgPSBtZXNzYWdlVGV4dDtcclxuXHJcbn1cclxuXHJcbi8vIFNob3cgYSBzcGlubmVyIG9uIHBheW1lbnQgc3VibWlzc2lvblxyXG5mdW5jdGlvbiBzZXRMb2FkaW5nKGlzTG9hZGluZykge1xyXG4gIGlmIChpc0xvYWRpbmcpIHsgXHJcbiAgICAvLyBEaXNhYmxlIHRoZSBidXR0b24gYW5kIHNob3cgYSBzcGlubmVyXHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI3N1Ym1pdFBheW1lbnRcIikuZGlzYWJsZWQgPSB0cnVlO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNzdWJtaXRQYXltZW50TW9iaWxlXCIpLmRpc2FibGVkID0gdHJ1ZTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjc3Bpbm5lclwiKS5jbGFzc0xpc3QucmVtb3ZlKFwiaGlkZGVuXCIpO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNzcGlubmVyTW9iaWxlXCIpLmNsYXNzTGlzdC5yZW1vdmUoXCJoaWRkZW5cIik7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI2J1dHRvbi10ZXh0XCIpLmNsYXNzTGlzdC5hZGQoXCJoaWRkZW5cIik7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI2J1dHRvbi10ZXh0LW1vYmlsZVwiKS5jbGFzc0xpc3QuYWRkKFwiaGlkZGVuXCIpO1xyXG4gIH0gZWxzZSB7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI3N1Ym1pdFBheW1lbnRcIikuZGlzYWJsZWQgPSBmYWxzZTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjc3VibWl0UGF5bWVudE1vYmlsZVwiKS5kaXNhYmxlZCA9IGZhbHNlO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNzcGlubmVyXCIpLmNsYXNzTGlzdC5hZGQoXCJoaWRkZW5cIik7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI3NwaW5uZXJNb2JpbGVcIikuY2xhc3NMaXN0LmFkZChcImhpZGRlblwiKTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjYnV0dG9uLXRleHRcIikuY2xhc3NMaXN0LnJlbW92ZShcImhpZGRlblwiKTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjYnV0dG9uLXRleHQtbW9iaWxlXCIpLmNsYXNzTGlzdC5hZGQoXCJoaWRkZW5cIik7XHJcbiAgfVxyXG59Il0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9