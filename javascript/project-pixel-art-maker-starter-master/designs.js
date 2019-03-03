// Select color input
let color = document.querySelector("#colorPicker")
// Select size input
const canvas = document.getElementById("pixelCanvas")
document.addEventListener("submit", function(event){//listens for submit button
    event.preventDefault();//prevent page from refreshing
    let height = document.getElementById("inputHeight").value//obtains selected height
    let width = document.getElementById("inputWidth").value//obtain selected width
    makeGrid(height, width);
})

function makeGrid(height,width) { //takes in height and width
    document.querySelector("table").innerHTML = ""//clears the table
    for (y = 1; y <= height; ++y){
        let row = document.createElement("tr") //creates a new row
        for (x = 1; x <= width; x++){
            let cell = document.createElement("td")// creates length of row
            cell.addEventListener("click", function colorcanvas(event){
            event.target.style.backgroundColor = color.value
            })//allow cell to change color
            row.appendChild(cell)// add cells to row
        canvas.appendChild(row)// adds row to table.
    }

  }
}
