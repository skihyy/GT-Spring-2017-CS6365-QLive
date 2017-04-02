/**
 * Created by yuyanghe on 2017/4/2.
 */
/**
 * Validate the form before submitted
 */
function validate() {
    var name = document.getElementById("nameInput").value;
    var pass = document.getElementById("passInput").value;
    var hashed_name_pass = hash(name + pass);
    document.getElementById("passInput").value = hashed_name_pass;
}

var I64BIT_TABLE =
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-'.split('');

/**
 * Using for hash password, providing a strong security.
 * @param input
 * @returns {string}
 */
function hash(input) {
    var hash = 5381;
    var i = input.length - 1;

    if (typeof input == 'string') {
        for (; i > -1; i--)
            hash += (hash << 5) + input.charCodeAt(i);
    }
    else {
        for (; i > -1; i--)
            hash += (hash << 5) + input[i];
    }
    var value = hash & 0x7FFFFFFF;

    var retValue = '';
    do {
        retValue += I64BIT_TABLE[value & 0x3F];
    }
    while (value >>= 6);

    return retValue;
}