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
      return_url: "https://checkmalt.herokuapp.com/checkout/confirmation/" + orderNumber,
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
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZGlzdC9zdHJpcGUuYnVuZGxlLmpzIiwibWFwcGluZ3MiOiI7Ozs7O0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsZUFBZTtBQUNmLEdBQUc7QUFDSCxVQUFVLDZCQUE2QjtBQUN2QztBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEtBQUs7QUFDTDtBQUNBLCtCQUErQiwwQkFBMEI7QUFDekQ7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsVUFBVSxRQUFRO0FBQ2xCO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsS0FBSztBQUNMLEdBQUc7QUFDSDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsVUFBVSxnQkFBZ0I7QUFDMUI7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLElBQUk7QUFDSjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9jaGVja21hbHRzLy4vY2hlY2tvdXQvc3RhdGljL2pzL3N0cmlwZV9lbGVtZW50cy5qcyJdLCJzb3VyY2VzQ29udGVudCI6WyJjb25zdCBzdHJpcGUgPSBTdHJpcGUoXCJwa190ZXN0XzUxS3l5TXRFVVNWVzdTejFzeTVKbDVMdTNWOFdhcmd4SEpoNHlmVUdLdXBQSVJ3WjdveHVycE1XZWRROXoxU1hpcHZ4TVRkS2s1VTJDeG5YVlZRMmNWMDVTMDBXQmtjeHJyalwiKTtcclxuXHJcblxyXG5cclxubGV0IGVsZW1lbnRzO1xyXG5sZXQgb3JkZXJOdW1iZXI7XHJcblxyXG5pbml0aWFsaXplKCk7XHJcbmNoZWNrU3RhdHVzKCk7XHJcblxyXG5kb2N1bWVudFxyXG4gIC5xdWVyeVNlbGVjdG9yKFwiI3BheW1lbnQtZm9ybVwiKVxyXG4gIC5hZGRFdmVudExpc3RlbmVyKFwic3VibWl0XCIsIGhhbmRsZVN1Ym1pdCk7XHJcblxyXG4vLyBGZXRjaGVzIGEgcGF5bWVudCBpbnRlbnQgYW5kIGNhcHR1cmVzIHRoZSBjbGllbnQgc2VjcmV0XHJcbmFzeW5jIGZ1bmN0aW9uIGluaXRpYWxpemUoKSB7XHJcbiAgY29uc3QgcmVzcG9uc2UgPSBhd2FpdCBmZXRjaChcImNyZWF0ZS1wYXltZW50LWludGVudFwiLCB7XHJcbiAgICBtZXRob2Q6IFwiUE9TVFwiLFxyXG4gICAgaGVhZGVyczogeyBcIkNvbnRlbnQtVHlwZVwiOiBcImFwcGxpY2F0aW9uL2pzb25cIiB9XHJcbiAgfSk7XHJcbiAgY29uc3QgeyBjbGllbnRTZWNyZXQsIG9yZGVyX251bWJlciB9ID0gYXdhaXQgcmVzcG9uc2UuanNvbigpO1xyXG4gIG9yZGVyTnVtYmVyID0gb3JkZXJfbnVtYmVyXHJcblxyXG4gIGNvbnN0IGFwcGVhcmFuY2UgPSB7XHJcbiAgICB0aGVtZTogJ25pZ2h0JyxcclxuICAgIGxhYmVsczogJ2Zsb2F0aW5nJyxcclxuICAgIHZhcmlhYmxlczoge1xyXG4gICAgICBjb2xvclByaW1hcnk6ICcjZmZmZmZmJyxcclxuICAgICAgY29sb3JCYWNrZ3JvdW5kOiAnIzAwMDAwMCcsXHJcbiAgICAgIGNvbG9yRGFuZ2VyOiAnI2ZmNTg1OCcsXHJcbiAgICAgIGNvbG9yRGFuZ2VyVGV4dDogJyNmZjU4NTgnXHJcbiAgICB9LFxyXG4gIH07XHJcbiAgZWxlbWVudHMgPSBzdHJpcGUuZWxlbWVudHMoeyBhcHBlYXJhbmNlLCBjbGllbnRTZWNyZXQgfSk7XHJcblxyXG4gIGNvbnN0IHBheW1lbnRFbGVtZW50ID0gZWxlbWVudHMuY3JlYXRlKFwicGF5bWVudFwiKTtcclxuICBwYXltZW50RWxlbWVudC5tb3VudChcIiNwYXltZW50LWVsZW1lbnRcIik7XHJcbn1cclxuXHJcbmFzeW5jIGZ1bmN0aW9uIGhhbmRsZVN1Ym1pdChlKSB7XHJcbiAgZS5wcmV2ZW50RGVmYXVsdCgpO1xyXG4gIHNldExvYWRpbmcodHJ1ZSk7XHJcblxyXG4gIGNvbnN0IHsgZXJyb3IgfSA9IGF3YWl0IHN0cmlwZS5jb25maXJtUGF5bWVudCh7XHJcbiAgICBlbGVtZW50cyxcclxuICAgIGNvbmZpcm1QYXJhbXM6IHtcclxuICAgICAgLy8gTWFrZSBzdXJlIHRvIGNoYW5nZSB0aGlzIHRvIHlvdXIgcGF5bWVudCBjb21wbGV0aW9uIHBhZ2VcclxuICAgICAgcmV0dXJuX3VybDogXCJodHRwczovL2NoZWNrbWFsdC5oZXJva3VhcHAuY29tL2NoZWNrb3V0L2NvbmZpcm1hdGlvbi9cIiArIG9yZGVyTnVtYmVyLFxyXG4gICAgfSxcclxuICB9KTtcclxuXHJcbiAgLy8gVGhpcyBwb2ludCB3aWxsIG9ubHkgYmUgcmVhY2hlZCBpZiB0aGVyZSBpcyBhbiBpbW1lZGlhdGUgZXJyb3Igd2hlblxyXG4gIC8vIGNvbmZpcm1pbmcgdGhlIHBheW1lbnQuIE90aGVyd2lzZSwgeW91ciBjdXN0b21lciB3aWxsIGJlIHJlZGlyZWN0ZWQgdG9cclxuICAvLyB5b3VyIGByZXR1cm5fdXJsYC4gRm9yIHNvbWUgcGF5bWVudCBtZXRob2RzIGxpa2UgaURFQUwsIHlvdXIgY3VzdG9tZXIgd2lsbFxyXG4gIC8vIGJlIHJlZGlyZWN0ZWQgdG8gYW4gaW50ZXJtZWRpYXRlIHNpdGUgZmlyc3QgdG8gYXV0aG9yaXplIHRoZSBwYXltZW50LCB0aGVuXHJcbiAgLy8gcmVkaXJlY3RlZCB0byB0aGUgYHJldHVybl91cmxgLlxyXG4gIGlmIChlcnJvci50eXBlID09PSBcImNhcmRfZXJyb3JcIiB8fCBlcnJvci50eXBlID09PSBcInZhbGlkYXRpb25fZXJyb3JcIikge1xyXG4gICAgc2hvd01lc3NhZ2UoZXJyb3IubWVzc2FnZSk7XHJcbiAgfSBlbHNlIHtcclxuICAgIHNob3dNZXNzYWdlKFwiQW4gdW5leHBlY3RlZCBlcnJvciBvY2N1cmVkLlwiKTtcclxuICB9XHJcblxyXG4gIHNldExvYWRpbmcoZmFsc2UpO1xyXG59XHJcblxyXG4vLyBGZXRjaGVzIHRoZSBwYXltZW50IGludGVudCBzdGF0dXMgYWZ0ZXIgcGF5bWVudCBzdWJtaXNzaW9uXHJcbmFzeW5jIGZ1bmN0aW9uIGNoZWNrU3RhdHVzKCkge1xyXG4gIGNvbnN0IGNsaWVudFNlY3JldCA9IG5ldyBVUkxTZWFyY2hQYXJhbXMod2luZG93LmxvY2F0aW9uLnNlYXJjaCkuZ2V0KFxyXG4gICAgXCJwYXltZW50X2ludGVudF9jbGllbnRfc2VjcmV0XCJcclxuICApO1xyXG5cclxuICBpZiAoIWNsaWVudFNlY3JldCkge1xyXG4gICAgcmV0dXJuO1xyXG4gIH1cclxuXHJcbiAgY29uc3QgeyBwYXltZW50SW50ZW50IH0gPSBhd2FpdCBzdHJpcGUucmV0cmlldmVQYXltZW50SW50ZW50KGNsaWVudFNlY3JldCk7XHJcblxyXG4gIHN3aXRjaCAocGF5bWVudEludGVudC5zdGF0dXMpIHtcclxuICAgIGNhc2UgXCJzdWNjZWVkZWRcIjpcclxuICAgICAgc2hvd01lc3NhZ2UoXCJQYXltZW50IHN1Y2NlZWRlZCFcIik7XHJcbiAgICAgIGJyZWFrO1xyXG4gICAgY2FzZSBcInByb2Nlc3NpbmdcIjpcclxuICAgICAgc2hvd01lc3NhZ2UoXCJZb3VyIHBheW1lbnQgaXMgcHJvY2Vzc2luZy5cIik7XHJcbiAgICAgIGJyZWFrO1xyXG4gICAgY2FzZSBcInJlcXVpcmVzX3BheW1lbnRfbWV0aG9kXCI6XHJcbiAgICAgIHNob3dNZXNzYWdlKFwiWW91ciBwYXltZW50IHdhcyBub3Qgc3VjY2Vzc2Z1bCwgcGxlYXNlIHRyeSBhZ2Fpbi5cIik7XHJcbiAgICAgIGJyZWFrO1xyXG4gICAgZGVmYXVsdDpcclxuICAgICAgc2hvd01lc3NhZ2UoXCJTb21ldGhpbmcgd2VudCB3cm9uZy5cIik7XHJcbiAgICAgIGJyZWFrO1xyXG4gIH1cclxufVxyXG5cclxuLy8gLS0tLS0tLSBVSSBoZWxwZXJzIC0tLS0tLS1cclxuXHJcbmZ1bmN0aW9uIHNob3dNZXNzYWdlKG1lc3NhZ2VUZXh0KSB7XHJcbiAgY29uc3QgbWVzc2FnZUNvbnRhaW5lciA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjcGF5bWVudC1tZXNzYWdlXCIpO1xyXG5cclxuICBtZXNzYWdlQ29udGFpbmVyLmNsYXNzTGlzdC5yZW1vdmUoXCJoaWRkZW5cIik7XHJcbiAgbWVzc2FnZUNvbnRhaW5lci5jbGFzc0xpc3QuYWRkKFwidGV4dC1yZWQtNzAwXCIpXHJcbiAgbWVzc2FnZUNvbnRhaW5lci50ZXh0Q29udGVudCA9IG1lc3NhZ2VUZXh0O1xyXG5cclxufVxyXG5cclxuLy8gU2hvdyBhIHNwaW5uZXIgb24gcGF5bWVudCBzdWJtaXNzaW9uXHJcbmZ1bmN0aW9uIHNldExvYWRpbmcoaXNMb2FkaW5nKSB7XHJcbiAgaWYgKGlzTG9hZGluZykgeyBcclxuICAgIC8vIERpc2FibGUgdGhlIGJ1dHRvbiBhbmQgc2hvdyBhIHNwaW5uZXJcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjc3VibWl0UGF5bWVudFwiKS5kaXNhYmxlZCA9IHRydWU7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI3N1Ym1pdFBheW1lbnRNb2JpbGVcIikuZGlzYWJsZWQgPSB0cnVlO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNzcGlubmVyXCIpLmNsYXNzTGlzdC5yZW1vdmUoXCJoaWRkZW5cIik7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI3NwaW5uZXJNb2JpbGVcIikuY2xhc3NMaXN0LnJlbW92ZShcImhpZGRlblwiKTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjYnV0dG9uLXRleHRcIikuY2xhc3NMaXN0LmFkZChcImhpZGRlblwiKTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjYnV0dG9uLXRleHQtbW9iaWxlXCIpLmNsYXNzTGlzdC5hZGQoXCJoaWRkZW5cIik7XHJcbiAgfSBlbHNlIHtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjc3VibWl0UGF5bWVudFwiKS5kaXNhYmxlZCA9IGZhbHNlO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNzdWJtaXRQYXltZW50TW9iaWxlXCIpLmRpc2FibGVkID0gZmFsc2U7XHJcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiI3NwaW5uZXJcIikuY2xhc3NMaXN0LmFkZChcImhpZGRlblwiKTtcclxuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXCIjc3Bpbm5lck1vYmlsZVwiKS5jbGFzc0xpc3QuYWRkKFwiaGlkZGVuXCIpO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNidXR0b24tdGV4dFwiKS5jbGFzc0xpc3QucmVtb3ZlKFwiaGlkZGVuXCIpO1xyXG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIiNidXR0b24tdGV4dC1tb2JpbGVcIikuY2xhc3NMaXN0LmFkZChcImhpZGRlblwiKTtcclxuICB9XHJcbn0iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=