function submit() {
    document.getElementById("json_data").value = JSON.stringify(js_data);
    document.getElementById("form").submit();
}

function set_global_eventlisteners() {

    document.getElementById("new_game_btn").addEventListener('click', event => {
        js_data["requested_action"] = "new_game";
        submit();
    })

    document.getElementById("run_stop_ai_btn").addEventListener('click', event => {
        let button_value = document.getElementById("run_stop_ai_btn").value
        if (button_value == "Run AI") {
            js_data["requested_action"] = "run_ai";

        } else {
            js_data["requested_action"] = "stop_ai";
            submit();
        }
    })

    //Disable default window scrolling on arrow-keys
    window.addEventListener("keydown", function(e) {
        if ([37, 38, 39, 40].indexOf(e.keyCode) > -1) {
            e.preventDefault();
        }
    }, false);
}


function set_human_agent_eventlisteners() {

    function human_move(direction) {
        js_data["direction"] = direction;
        js_data["requested_action"] = "human_move"
        submit()
    }

    document.addEventListener('keydown', event => {
        switch (event.keyCode) {
            case 37:
                human_move("l");
                console.log("LEFT")
                break;

            case 39:
                human_move("r");
                break;

            case 38:
                human_move("u");
                break;

            case 40:
                human_move("d");
                break;
        }
    });
}