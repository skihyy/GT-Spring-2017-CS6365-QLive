/**
 * Created by yuyanghe on 2017/4/2.
 */
var messageBox = null;

function sendMsg() {
    var content = document.getElementById("contentBox").value;
    document.getElementById("contentBox").value = "";
    sender.publish({
        channel: channel,
        message: content
    });
    appendToMessageBox(content);
}

function appendToMessageBox(content) {
    if (null == messageBox) {
        messageBox = document.getElementById("messageBox");
    }
    if("endsessionendsessionendsessionendsession" == content){
        alert('<This session has been ended by the host. Thank you for joining the session.>');
        return;
    }
    var newDiv = document.createElement("div");
    var newSpan = document.createElement("span");
    newSpan.setAttribute("class", "messageContent");
    newSpan.innerText = content;
    newDiv.appendChild(newSpan);
    messageBox.appendChild(newDiv);
}

if (window.event.keyCode == 13) {
    sendMsg();
}

function endSession() {
    if(confirm('Are you sure to end current live session?')){
        sender.publish({
            channel: channel,
            message: "endsessionendsessionendsessionendsession"
        });
        return true;
    }
    return false;
}