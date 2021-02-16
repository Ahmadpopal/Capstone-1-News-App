// Select published Time by class name 
const times = document.querySelectorAll(".time")


// Function to change Published Date & Time to Human readable
function dateTimeReader(time){
    // GET the Time 
    let timeToArraySliceTime = time.split('-').slice(2)
    let toString = timeToArraySliceTime.join('')
    let timeOutPut  = toString.slice(3, 8)
    // GET DATE
    let dateYearMonth= time.split('-').slice(0, 2)
    let sliceDayFromTime = time.split('-').slice(2).join('')
    let day = sliceDayFromTime.slice(0, 2);
    dateYearMonth.push(day)

        return `Posted: ${dateYearMonth} Time: ${timeOutPut} CST`
    } 

    // Set Publish time to Human readable 
    for(let time of times){
        console.log(time.innerHTML)
        time.innerHTML = dateTimeReader(time.innerHTML)
    }



