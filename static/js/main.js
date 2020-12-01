set_global_eventlisteners()

if(js_data['game_over']){
    document.getElementById("game-over-message").innerHTML = "GAME OVER";
    document.getElementById("run_stop_ai_btn").disabled ='True';
}

if(js_data['agent'] == 'human' && !js_data['game_over']){
    set_human_agent_eventlisteners()
}

if(js_data['agent'] == 'ai'){
    submit()
}

let width = (window.innerWidth > 0) ? window.innerWidth : screen.width;
let height = (window.innerHeight > 0) ? window.innerHeight : screen.height;

if(width < 370){
    document.getElementsByTagName("body")[0].innerHTML= "Your screen is to small for this game. Sorry."
}

// I screen is not very heigh, move the view to the grid area after moves are made
if(height < 575){
    if(js_data["requested_action"] != "new_game"){
            window.location = "#grid";
        }
    }
