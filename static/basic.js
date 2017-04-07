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

/**
 * Validate the balance of user before joining a live session.
 * @param price price of live session
 * @param balance balance in one's account
 * @returns whether the balance can afford the price
 */
function checkValidation(price, balance)
{
    if(price > balance)
    {
        alert("There is no enough balance in your account.");
        return false;
    }
    return true;
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