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
/******/ })()
;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZGlzdC9zdHJpcGUuYnVuZGxlLmpzIiwibWFwcGluZ3MiOiI7Ozs7O0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsZUFBZTtBQUNmLEdBQUc7QUFDSCxVQUFVLDZCQUE2QjtBQUN2QztBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEtBQUs7QUFDTDtBQUNBLCtCQUErQiwwQkFBMEI7QUFDekQ7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsVUFBVSxRQUFRO0FBQ2xCO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxLQUFLO0FBQ0wsR0FBRztBQUNIO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxJQUFJO0FBQ0o7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxVQUFVLGdCQUFnQjtBQUMxQjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsQyIsInNvdXJjZXMiOlsid2VicGFjazovL2NoZWNrbWFsdHMvLi9jaGVja291dC9zdGF0aWMvanMvc3RyaXBlX2VsZW1lbnRzLmpzIl0sInNvdXJjZXNDb250ZW50IjpbImNvbnN0IHN0cmlwZSA9IFN0cmlwZShcInBrX3Rlc3RfNTFLeXlNdEVVU1ZXN1N6MXN5NUpsNUx1M1Y4V2FyZ3hISmg0eWZVR0t1cFBJUndaN294dXJwTVdlZFE5ejFTWGlwdnhNVGRLazVVMkN4blhWVlEyY1YwNVMwMFdCa2N4cnJqXCIpO1xyXG5cclxuXHJcblxyXG5sZXQgZWxlbWVudHM7XHJcbmxldCBvcmRlck51bWJlcjtcclxuXHJcbmluaXRpYWxpemUoKTtcclxuY2hlY2tTdGF0dXMoKTtcclxuXHJcbmRvY3VtZW50XHJcbiAgLnF1ZXJ5U2VsZWN0b3IoXCIjcGF5bWVudC1mb3JtXCIpXHJcbiAgLmFkZEV2ZW50TGlzdGVuZXIoXCJzdWJtaXRcIiwgaGFuZGxlU3VibWl0KTtcclxuXHJcbi8vIEZldGNoZXMgYSBwYXltZW50IGludGVudCBhbmQgY2FwdHVyZXMgdGhlIGNsaWVudCBzZWNyZXRcclxuYXN5bmMgZnVuY3Rpb24gaW5pdGlhbGl6ZSgpIHtcclxuICBjb25zdCByZXNwb25zZSA9IGF3YWl0IGZldGNoKFwiY3JlYXRlLXBheW1lbnQtaW50ZW50XCIsIHtcclxuICAgIG1ldGhvZDogXCJQT1NUXCIsXHJcbiAgICBoZWFkZXJzOiB7IFwiQ29udGVudC1UeXBlXCI6IFwiYXBwbGljYXRpb24vanNvblwiIH1cclxuICB9KTtcclxuICBjb25zdCB7IGNsaWVudFNlY3JldCwgb3JkZXJfbnVtYmVyIH0gPSBhd2FpdCByZXNwb25zZS5qc29uKCk7XHJcbiAgb3JkZXJOdW1iZXIgPSBvcmRlcl9udW1iZXJcclxuXHJcbiAgY29uc3QgYXBwZWFyYW5jZSA9IHtcclxuICAgIHRoZW1lOiAnbmlnaHQnLFxyXG4gICAgbGFiZWxzOiAnZmxvYXRpbmcnLFxyXG4gICAgdmFyaWFibGVzOiB7XHJcbiAgICAgIGNvbG9yUHJpbWFyeTogJyNmZmZmZmYnLFxyXG4gICAgICBjb2xvckJhY2tncm91bmQ6ICcjMDAwMDAwJyxcclxuICAgICAgY29sb3JEYW5nZXI6ICcjZmY1ODU4JyxcclxuICAgICAgY29sb3JEYW5nZXJUZXh0OiAnI2ZmNTg1OCdcclxuICAgIH0sXHJcbiAgfTtcclxuICBlbGVtZW50cyA9IHN0cmlwZS5lbGVtZW50cyh7IGFwcGVhcmFuY2UsIGNsaWVudFNlY3JldCB9KTtcclxuXHJcbiAgY29uc3QgcGF5bWVudEVsZW1lbnQgPSBlbGVtZW50cy5jcmVhdGUoXCJwYXltZW50XCIpO1xyXG4gIHBheW1lbnRFbGVtZW50Lm1vdW50KFwiI3BheW1lbnQtZWxlbWVudFwiKTtcclxufVxyXG5cclxuYXN5bmMgZnVuY3Rpb24gaGFuZGxlU3VibWl0KGUpIHtcclxuICBlLnByZXZlbnREZWZhdWx0KCk7XHJcbiAgc2V0TG9hZGluZyh0cnVlKTtcclxuXHJcbiAgY29uc3QgeyBlcnJvciB9ID0gYXdhaXQgc3RyaXBlLmNvbmZpcm1QYXltZW50KHtcclxuICAgIGVsZW1lbnRzLFxyXG4gICAgY29uZmlybVBhcmFtczoge1xyXG4gICAgICAvLyBNYWtlIHN1cmUgdG8gY2hhbmdlIHRoaXMgdG8geW91ciBwYXltZW50IGNvbXBsZXRpb24gcGFnZVxyXG4gICAgICAvLyByZXR1cm5fdXJsOiBcImh0dHBzOi8vY2hlY2ttYWx0Lmhlcm9rdWFwcC5jb20vY2hlY2tvdXQvY29uZmlybWF0aW9uL1wiICsgb3JkZXJOdW1iZXIsIC8vdW5jb21tZW50IHRoaXMgbGluZSBpbiBwcm9kdWN0aW9uXHJcbiAgICAgIHJldHVybl91cmw6IFwiaHR0cDovLzEyNy4wLjAuMTo4MDAwL2NoZWNrb3V0L2NvbmZpcm1hdGlvbi9cIiArIG9yZGVyTnVtYmVyLCAvLyBjb21tZW50IHRoaXMgbGluZSBpbiBwcm9kdWN0aW9uXHJcbiAgICB9LFxyXG4gIH0pO1xyXG5cclxuICAvLyBUaGlzIHBvaW50IHdpbGwgb25seSBiZSByZWFjaGVkIGlmIHRoZXJlIGlzIGFuIGltbWVkaWF0ZSBlcnJvciB3aGVuXHJcbiAgLy8gY29uZmlybWluZyB0aGUgcGF5bWVudC4gT3RoZXJ3aXNlLCB5b3VyIGN1c3RvbWVyIHdpbGwgYmUgcmVkaXJlY3RlZCB0b1xyXG4gIC8vIHlvdXIgYHJldHVybl91cmxgLiBGb3Igc29tZSBwYXltZW50IG1ldGhvZHMgbGlrZSBpREVBTCwgeW91ciBjdXN0b21lciB3aWxsXHJcbiAgLy8gYmUgcmVkaXJlY3RlZCB0byBhbiBpbnRlcm1lZGlhdGUgc2l0ZSBmaXJzdCB0byBhdXRob3JpemUgdGhlIHBheW1lbnQsIHRoZW5cclxuICAvLyByZWRpcmVjdGVkIHRvIHRoZSBgcmV0dXJuX3VybGAuXHJcbiAgaWYgKGVycm9yLnR5cGUgPT09IFwiY2FyZF9lcnJvclwiIHx8IGVycm9yLnR5cGUgPT09IFwidmFsaWRhdGlvbl9lcnJvclwiKSB7XHJcbiAgICBzaG93TWVzc2FnZShlcnJvci5tZXNzYWdlKTtcclxuICB9IGVsc2Uge1xyXG4gICAgc2hvd01lc3NhZ2UoXCJBbiB1bmV4cGVjdGVkIGVycm9yIG9jY3VyZWQuXCIpO1xyXG4gIH1cclxuXHJcbiAgc2V0TG9hZGluZyhmYWxzZSk7XHJcbn1cclxuXHJcbi8vIEZldGNoZXMgdGhlIHBheW1lbnQgaW50ZW50IHN0YXR1cyBhZnRlciBwYXltZW50IHN1Ym1pc3Npb25cclxuYXN5bmMgZnVuY3Rpb24gY2hlY2tTdGF0dXMoKSB7XHJcbiAgY29uc3QgY2xpZW50U2VjcmV0ID0gbmV3IFVSTFNlYXJjaFBhcmFtcyh3aW5kb3cubG9jYXRpb24uc2VhcmNoKS5nZXQoXHJcbiAgICBcInBheW1lbnRfaW50ZW50X2NsaWVudF9zZWNyZXRcIlxyXG4gICk7XHJcblxyXG4gIGlmICghY2xpZW50U2VjcmV0KSB7XHJcbiAgICByZXR1cm47XHJcbiAgfVxyXG5cclxuICBjb25zdCB7IHBheW1lbnRJbnRlbnQgfSA9IGF3YWl0IHN0cmlwZS5yZXRyaWV2ZVBheW1lbnRJbnRlbnQoY2xpZW50U2VjcmV0KTtcclxuXHJcbiAgc3dpdGNoIChwYXltZW50SW50ZW50LnN0YXR1cykge1xyXG4gICAgY2FzZSBcInN1Y2NlZWRlZFwiOlxyXG4gICAgICBzaG93TWVzc2FnZShcIlBheW1lbnQgc3VjY2VlZGVkIVwiKTtcclxuICAgICAgYnJlYWs7XHJcbiAgICBjYXNlIFwicHJvY2Vzc2luZ1wiOlxyXG4gICAgICBzaG93TWVzc2FnZShcIllvdXIgcGF5bWVudCBpcyBwcm9jZXNzaW5nLlwiKTtcclxuICAgICAgYnJlYWs7XHJcbiAgICBjYXNlIFwicmVxdWlyZXNfcGF5bWVudF9tZXRob2RcIjpcclxuICAgICAgc2hvd01lc3NhZ2UoXCJZb3VyIHBheW1lbnQgd2FzIG5vdCBzdWNjZXNzZnVsLCBwbGVhc2UgdHJ5IGFnYWluLlwiKTtcclxuICAgICAgYnJlYWs7XHJcbiAgICBkZWZhdWx0OlxyXG4gICAgICBzaG93TWVzc2FnZShcIlNvbWV0aGluZyB3ZW50IHdyb25nLlwiKTtcclxuICAgICAgYnJlYWs7XHJcbiAgfVxyXG59XHJcblxyXG4vLyAtLS0tLS0tIFVJIGhlbHBlcnMgLS0tLS0tLVxyXG5cclxuZnVuY3Rpb24gc2hvd01lc3NhZ2UobWVzc2FnZVRleHQpIHtcclxuICBjb25zdCBtZXNzYWdlQ29udGFpbmVyID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNwYXltZW50LW1lc3NhZ2VcIik7XHJcblxyXG4gIG1lc3NhZ2VDb250YWluZXIuY2xhc3NMaXN0LnJlbW92ZShcImhpZGRlblwiKTtcclxuICBtZXNzYWdlQ29udGFpbmVyLmNsYXNzTGlzdC5hZGQoXCJ0ZXh0LXJlZC03MDBcIilcclxuICBtZXNzYWdlQ29udGFpbmVyLnRleHRDb250ZW50ID0gbWVzc2FnZVRleHQ7XHJcblxyXG59XHJcblxyXG4vLyBTaG93IGEgc3Bpbm5lciBvbiBwYXltZW50IHN1Ym1pc3Npb25cclxuZnVuY3Rpb24gc2V0TG9hZGluZyhpc0xvYWRpbmcpIHtcclxuICBpZiAoaXNMb2FkaW5nKSB7IFxyXG4gICAgLy8gRGlzYWJsZSB0aGUgYnV0dG9uIGFuZCBzaG93IGEgc3Bpbm5lclxyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNzdWJtaXRQYXltZW50XCIpLmRpc2FibGVkID0gdHJ1ZTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjc3VibWl0UGF5bWVudE1vYmlsZVwiKS5kaXNhYmxlZCA9IHRydWU7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI3NwaW5uZXJcIikuY2xhc3NMaXN0LnJlbW92ZShcImhpZGRlblwiKTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjc3Bpbm5lck1vYmlsZVwiKS5jbGFzc0xpc3QucmVtb3ZlKFwiaGlkZGVuXCIpO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNidXR0b24tdGV4dFwiKS5jbGFzc0xpc3QuYWRkKFwiaGlkZGVuXCIpO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNidXR0b24tdGV4dC1tb2JpbGVcIikuY2xhc3NMaXN0LmFkZChcImhpZGRlblwiKTtcclxuICB9IGVsc2Uge1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNzdWJtaXRQYXltZW50XCIpLmRpc2FibGVkID0gZmFsc2U7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI3N1Ym1pdFBheW1lbnRNb2JpbGVcIikuZGlzYWJsZWQgPSBmYWxzZTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjc3Bpbm5lclwiKS5jbGFzc0xpc3QuYWRkKFwiaGlkZGVuXCIpO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNzcGlubmVyTW9iaWxlXCIpLmNsYXNzTGlzdC5hZGQoXCJoaWRkZW5cIik7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI2J1dHRvbi10ZXh0XCIpLmNsYXNzTGlzdC5yZW1vdmUoXCJoaWRkZW5cIik7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI2J1dHRvbi10ZXh0LW1vYmlsZVwiKS5jbGFzc0xpc3QuYWRkKFwiaGlkZGVuXCIpO1xyXG4gIH1cclxufSJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==