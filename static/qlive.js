/**
 * Created by yuyanghe on 2017/4/2.
 */
var sender = null;
var messageBox = null;
function sendMsg(appkey) {
    if (null == sender) {
        sender = new GoEasy({
            appkey: appkey
        });
    }
    var content = document.getElementById("contentBox").value;
    document.getElementById("contentBox").value = "";
    sender.publish({
            channel: 'demo_channel',
            message: content
        });
    appendToMessageBox(content);
}

function appendToMessageBox(content)
{
    if(null == messageBox)
    {
        messageBox = document.getElementById("messageBox");
    }
    var newDiv = document.createElement("div");
    var newSpan = document.createElement("span");
    newSpan.setAttribute("class", "messageContent");
    newSpan.innerText = content;
    newDiv.appendChild(newSpan);
    messageBox.appendChild(newDiv);
}