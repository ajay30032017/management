var updateBtns = document.getElementsByClassName('update-list');


for(var i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){

        var productID = this.dataset.product;
        var action = this.dataset.action;
        console.log('product:',productID,'action :',action);
        console.log('user',user);
            if(user == "AnonymousUser"){
                console.log("you are not logged in!")
            }
            else{
                updateUserOrder(productID,action);
            }

    })
}

function updateUserOrder(productID,action){
    console.log('user is logged in, sending data')
    url = '/update_list/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'productID':productID,'action':action
        })
    })
        .then((response) =>
        {
            return response.json()
        })
        .then((data) =>
        {
            console.log('data',data)

        })

    
}