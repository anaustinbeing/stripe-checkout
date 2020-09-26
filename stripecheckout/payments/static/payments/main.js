console.log('sanity check')

fetch('/config/')
.then((result) => { return result.json(); })
.then((data) => { 
    const stripe =  Stripe(data.publish_key); 

    var buttonListener = document.querySelector("#submitBtn")
    if(buttonListener){
        buttonListener.addEventListener("click", () => {
        fetch('/create_session/')
        .then((result) => { return result.json() })

        .then((data) => {
            stripe.redirectToCheckout({'sessionId': data.sessionId})
        })
        .then((res) => { console.log(res) })
        })
    }
})
//})
//}