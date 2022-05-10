console.log("im here");

let updateCartBtn=document.getElementsByClassName("update-cart");
for(let key of updateCartBtn ){
    key.addEventListener("click",function(){
        let productId=this.dataset.product;
        let action=this.dataset.action;
        if(user==="AnonymousUser"){
            addCookieItem(productId,action);
        }
        else{
            updateItemFunction(productId,action);
        }
    });
}


function addCookieItem(productId,action) {

    if (action == "add"){
		if (cart[productId] == undefined){
		cart[productId] = {"quantity":1}

		}else{
			cart[productId]["quantity"] += 1
		}
	}

    if (action == 'remove'){
		cart[productId]["quantity"] -= 1

		if (cart[productId]["quantity"] <= 0){
			console.log("Item should be deleted")
			delete cart[productId];
		}
	}
    console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()

}


function updateItemFunction(productId,action) {
    let url="/update_item/"
    fetch(url,{
        method:"POST",
        headers:{
            "Content-Type":"application/json",
            "X-CSRFToken":csrftoken,
        },
        body:JSON.stringify({"productId":productId,"action":action})
    }).then(response=>response.json())
    .then((data)=>{
        console.log("data:",data)
        location.reload()
    })
}
