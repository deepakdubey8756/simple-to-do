function handleClick(value){
    console.log("HandleClick is initiated", value)
    const element = document.getElementsByClassName(`myform${value}`)[0]
    console.log(element)
    element.click()
}