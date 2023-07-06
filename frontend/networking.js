/*
=========================================================================================
Define a general request function
=========================================================================================
*/

function request(endpoint, mode, callback, body = {}) {
    // creates an xmlhttp request
    var xmlhttp = new XMLHttpRequest();
    // when the page is ready
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            callback(JSON.parse(this.responseText));
        }
    };
    // access this url
    var url = "http://localhost:5000/";
    url += endpoint;
    xmlhttp.open(mode, url, true);
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.send(JSON.stringify(body));
}

/*
=========================================================================================
Request functions
=========================================================================================
*/

let exportWalk

export function generateRandomWalk(shape, size) {
    let request_body = {
        "shape": shape,
        "size": size
    };
    request("generateRandomWalk", "POST", returnWalk, request_body);
}

function returnWalk(response) {
    console.log(response["walk"])
    exportWalk = response["walk"]
}

export { exportWalk }