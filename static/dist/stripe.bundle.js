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
      return_url: "http://127.0.0.1:8000/checkout/confirmation/" + orderNumber,
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
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZGlzdC9zdHJpcGUuYnVuZGxlLmpzIiwibWFwcGluZ3MiOiI7Ozs7O0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsZUFBZTtBQUNmLEdBQUc7QUFDSCxVQUFVLDZCQUE2QjtBQUN2QztBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEtBQUs7QUFDTDtBQUNBLCtCQUErQiwwQkFBMEI7QUFDekQ7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsVUFBVSxRQUFRO0FBQ2xCO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsS0FBSztBQUNMLEdBQUc7QUFDSDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsVUFBVSxnQkFBZ0I7QUFDMUI7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLElBQUk7QUFDSjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9jaGVja21hbHRzLy4vY2hlY2tvdXQvc3RhdGljL2pzL3N0cmlwZV9lbGVtZW50cy5qcyJdLCJzb3VyY2VzQ29udGVudCI6WyJjb25zdCBzdHJpcGUgPSBTdHJpcGUoXCJwa190ZXN0XzUxS3l5TXRFVVNWVzdTejFzeTVKbDVMdTNWOFdhcmd4SEpoNHlmVUdLdXBQSVJ3WjdveHVycE1XZWRROXoxU1hpcHZ4TVRkS2s1VTJDeG5YVlZRMmNWMDVTMDBXQmtjeHJyalwiKTtcclxuXHJcblxyXG5cclxubGV0IGVsZW1lbnRzO1xyXG5sZXQgb3JkZXJOdW1iZXI7XHJcblxyXG5pbml0aWFsaXplKCk7XHJcbmNoZWNrU3RhdHVzKCk7XHJcblxyXG5kb2N1bWVudFxyXG4gIC5xdWVyeVNlbGVjdG9yKFwiI3BheW1lbnQtZm9ybVwiKVxyXG4gIC5hZGRFdmVudExpc3RlbmVyKFwic3VibWl0XCIsIGhhbmRsZVN1Ym1pdCk7XHJcblxyXG4vLyBGZXRjaGVzIGEgcGF5bWVudCBpbnRlbnQgYW5kIGNhcHR1cmVzIHRoZSBjbGllbnQgc2VjcmV0XHJcbmFzeW5jIGZ1bmN0aW9uIGluaXRpYWxpemUoKSB7XHJcbiAgY29uc3QgcmVzcG9uc2UgPSBhd2FpdCBmZXRjaChcImNyZWF0ZS1wYXltZW50LWludGVudFwiLCB7XHJcbiAgICBtZXRob2Q6IFwiUE9TVFwiLFxyXG4gICAgaGVhZGVyczogeyBcIkNvbnRlbnQtVHlwZVwiOiBcImFwcGxpY2F0aW9uL2pzb25cIiB9XHJcbiAgfSk7XHJcbiAgY29uc3QgeyBjbGllbnRTZWNyZXQsIG9yZGVyX251bWJlciB9ID0gYXdhaXQgcmVzcG9uc2UuanNvbigpO1xyXG4gIG9yZGVyTnVtYmVyID0gb3JkZXJfbnVtYmVyXHJcblxyXG4gIGNvbnN0IGFwcGVhcmFuY2UgPSB7XHJcbiAgICB0aGVtZTogJ25pZ2h0JyxcclxuICAgIGxhYmVsczogJ2Zsb2F0aW5nJyxcclxuICAgIHZhcmlhYmxlczoge1xyXG4gICAgICBjb2xvclByaW1hcnk6ICcjZmZmZmZmJyxcclxuICAgICAgY29sb3JCYWNrZ3JvdW5kOiAnIzAwMDAwMCcsXHJcbiAgICAgIGNvbG9yRGFuZ2VyOiAnI2ZmNTg1OCcsXHJcbiAgICAgIGNvbG9yRGFuZ2VyVGV4dDogJyNmZjU4NTgnXHJcbiAgICB9LFxyXG4gIH07XHJcbiAgZWxlbWVudHMgPSBzdHJpcGUuZWxlbWVudHMoeyBhcHBlYXJhbmNlLCBjbGllbnRTZWNyZXQgfSk7XHJcblxyXG4gIGNvbnN0IHBheW1lbnRFbGVtZW50ID0gZWxlbWVudHMuY3JlYXRlKFwicGF5bWVudFwiKTtcclxuICBwYXltZW50RWxlbWVudC5tb3VudChcIiNwYXltZW50LWVsZW1lbnRcIik7XHJcbn1cclxuXHJcbmFzeW5jIGZ1bmN0aW9uIGhhbmRsZVN1Ym1pdChlKSB7XHJcbiAgZS5wcmV2ZW50RGVmYXVsdCgpO1xyXG4gIHNldExvYWRpbmcodHJ1ZSk7XHJcblxyXG4gIGNvbnN0IHsgZXJyb3IgfSA9IGF3YWl0IHN0cmlwZS5jb25maXJtUGF5bWVudCh7XHJcbiAgICBlbGVtZW50cyxcclxuICAgIGNvbmZpcm1QYXJhbXM6IHtcclxuICAgICAgLy8gTWFrZSBzdXJlIHRvIGNoYW5nZSB0aGlzIHRvIHlvdXIgcGF5bWVudCBjb21wbGV0aW9uIHBhZ2VcclxuICAgICAgcmV0dXJuX3VybDogXCJodHRwOi8vMTI3LjAuMC4xOjgwMDAvY2hlY2tvdXQvY29uZmlybWF0aW9uL1wiICsgb3JkZXJOdW1iZXIsXHJcbiAgICB9LFxyXG4gIH0pO1xyXG5cclxuICAvLyBUaGlzIHBvaW50IHdpbGwgb25seSBiZSByZWFjaGVkIGlmIHRoZXJlIGlzIGFuIGltbWVkaWF0ZSBlcnJvciB3aGVuXHJcbiAgLy8gY29uZmlybWluZyB0aGUgcGF5bWVudC4gT3RoZXJ3aXNlLCB5b3VyIGN1c3RvbWVyIHdpbGwgYmUgcmVkaXJlY3RlZCB0b1xyXG4gIC8vIHlvdXIgYHJldHVybl91cmxgLiBGb3Igc29tZSBwYXltZW50IG1ldGhvZHMgbGlrZSBpREVBTCwgeW91ciBjdXN0b21lciB3aWxsXHJcbiAgLy8gYmUgcmVkaXJlY3RlZCB0byBhbiBpbnRlcm1lZGlhdGUgc2l0ZSBmaXJzdCB0byBhdXRob3JpemUgdGhlIHBheW1lbnQsIHRoZW5cclxuICAvLyByZWRpcmVjdGVkIHRvIHRoZSBgcmV0dXJuX3VybGAuXHJcbiAgaWYgKGVycm9yLnR5cGUgPT09IFwiY2FyZF9lcnJvclwiIHx8IGVycm9yLnR5cGUgPT09IFwidmFsaWRhdGlvbl9lcnJvclwiKSB7XHJcbiAgICBzaG93TWVzc2FnZShlcnJvci5tZXNzYWdlKTtcclxuICB9IGVsc2Uge1xyXG4gICAgc2hvd01lc3NhZ2UoXCJBbiB1bmV4cGVjdGVkIGVycm9yIG9jY3VyZWQuXCIpO1xyXG4gIH1cclxuXHJcbiAgc2V0TG9hZGluZyhmYWxzZSk7XHJcbn1cclxuXHJcbi8vIEZldGNoZXMgdGhlIHBheW1lbnQgaW50ZW50IHN0YXR1cyBhZnRlciBwYXltZW50IHN1Ym1pc3Npb25cclxuYXN5bmMgZnVuY3Rpb24gY2hlY2tTdGF0dXMoKSB7XHJcbiAgY29uc3QgY2xpZW50U2VjcmV0ID0gbmV3IFVSTFNlYXJjaFBhcmFtcyh3aW5kb3cubG9jYXRpb24uc2VhcmNoKS5nZXQoXHJcbiAgICBcInBheW1lbnRfaW50ZW50X2NsaWVudF9zZWNyZXRcIlxyXG4gICk7XHJcblxyXG4gIGlmICghY2xpZW50U2VjcmV0KSB7XHJcbiAgICByZXR1cm47XHJcbiAgfVxyXG5cclxuICBjb25zdCB7IHBheW1lbnRJbnRlbnQgfSA9IGF3YWl0IHN0cmlwZS5yZXRyaWV2ZVBheW1lbnRJbnRlbnQoY2xpZW50U2VjcmV0KTtcclxuXHJcbiAgc3dpdGNoIChwYXltZW50SW50ZW50LnN0YXR1cykge1xyXG4gICAgY2FzZSBcInN1Y2NlZWRlZFwiOlxyXG4gICAgICBzaG93TWVzc2FnZShcIlBheW1lbnQgc3VjY2VlZGVkIVwiKTtcclxuICAgICAgYnJlYWs7XHJcbiAgICBjYXNlIFwicHJvY2Vzc2luZ1wiOlxyXG4gICAgICBzaG93TWVzc2FnZShcIllvdXIgcGF5bWVudCBpcyBwcm9jZXNzaW5nLlwiKTtcclxuICAgICAgYnJlYWs7XHJcbiAgICBjYXNlIFwicmVxdWlyZXNfcGF5bWVudF9tZXRob2RcIjpcclxuICAgICAgc2hvd01lc3NhZ2UoXCJZb3VyIHBheW1lbnQgd2FzIG5vdCBzdWNjZXNzZnVsLCBwbGVhc2UgdHJ5IGFnYWluLlwiKTtcclxuICAgICAgYnJlYWs7XHJcbiAgICBkZWZhdWx0OlxyXG4gICAgICBzaG93TWVzc2FnZShcIlNvbWV0aGluZyB3ZW50IHdyb25nLlwiKTtcclxuICAgICAgYnJlYWs7XHJcbiAgfVxyXG59XHJcblxyXG4vLyAtLS0tLS0tIFVJIGhlbHBlcnMgLS0tLS0tLVxyXG5cclxuZnVuY3Rpb24gc2hvd01lc3NhZ2UobWVzc2FnZVRleHQpIHtcclxuICBjb25zdCBtZXNzYWdlQ29udGFpbmVyID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNwYXltZW50LW1lc3NhZ2VcIik7XHJcblxyXG4gIG1lc3NhZ2VDb250YWluZXIuY2xhc3NMaXN0LnJlbW92ZShcImhpZGRlblwiKTtcclxuICBtZXNzYWdlQ29udGFpbmVyLmNsYXNzTGlzdC5hZGQoXCJ0ZXh0LXJlZC03MDBcIilcclxuICBtZXNzYWdlQ29udGFpbmVyLnRleHRDb250ZW50ID0gbWVzc2FnZVRleHQ7XHJcblxyXG59XHJcblxyXG4vLyBTaG93IGEgc3Bpbm5lciBvbiBwYXltZW50IHN1Ym1pc3Npb25cclxuZnVuY3Rpb24gc2V0TG9hZGluZyhpc0xvYWRpbmcpIHtcclxuICBpZiAoaXNMb2FkaW5nKSB7IFxyXG4gICAgLy8gRGlzYWJsZSB0aGUgYnV0dG9uIGFuZCBzaG93IGEgc3Bpbm5lclxyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNzdWJtaXRQYXltZW50XCIpLmRpc2FibGVkID0gdHJ1ZTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjc3VibWl0UGF5bWVudE1vYmlsZVwiKS5kaXNhYmxlZCA9IHRydWU7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI3NwaW5uZXJcIikuY2xhc3NMaXN0LnJlbW92ZShcImhpZGRlblwiKTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjc3Bpbm5lck1vYmlsZVwiKS5jbGFzc0xpc3QucmVtb3ZlKFwiaGlkZGVuXCIpO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNidXR0b24tdGV4dFwiKS5jbGFzc0xpc3QuYWRkKFwiaGlkZGVuXCIpO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNidXR0b24tdGV4dC1tb2JpbGVcIikuY2xhc3NMaXN0LmFkZChcImhpZGRlblwiKTtcclxuICB9IGVsc2Uge1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNzdWJtaXRQYXltZW50XCIpLmRpc2FibGVkID0gZmFsc2U7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI3N1Ym1pdFBheW1lbnRNb2JpbGVcIikuZGlzYWJsZWQgPSBmYWxzZTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjc3Bpbm5lclwiKS5jbGFzc0xpc3QuYWRkKFwiaGlkZGVuXCIpO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNzcGlubmVyTW9iaWxlXCIpLmNsYXNzTGlzdC5hZGQoXCJoaWRkZW5cIik7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI2J1dHRvbi10ZXh0XCIpLmNsYXNzTGlzdC5yZW1vdmUoXCJoaWRkZW5cIik7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI2J1dHRvbi10ZXh0LW1vYmlsZVwiKS5jbGFzc0xpc3QuYWRkKFwiaGlkZGVuXCIpO1xyXG4gIH1cclxufSJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==