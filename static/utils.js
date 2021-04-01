function get_height() {
    return window.innerHeight;
}

function post(url, params) {
    var temp = document.createElement("form");
    temp.action = url;
    temp.method = "post";
    temp.style.display = "none";
    for (var x in params) {
        var opt = document.createElement("input");
        opt.name = x;
        opt.value = params[x];
        temp.appendChild(opt);
    }
    document.body.appendChild(temp);
    temp.submit();
    return temp;
}

function image_clicked(img_id) {
    post('set_error', {img_id: img_id});
}

function show_image(MEDIA_URL, img, img_id, height) {
    document.writeln(
        "<button onclick='image_clicked(", img_id, ")' style=\"height: 100%; width: 100%;\">" +
        "<img src=\"", MEDIA_URL, img, "\" style=\"height: ", height/6, "px; width: 100%;\">" +
        "</button>"
    );
}

function all_correct_clicked(class_index) {
    post('set_correct', {class_index: class_index})
}
