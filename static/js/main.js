set_global_eventlisteners()

console.log(js_data)

if (js_data['game_over']) {
    document.getElementById("game-over-message").innerHTML = "GAME OVER";
    document.getElementById("run_stop_ai_btn").disabled = 'True';
}

if (js_data['agent'] == 'human' && !js_data['game_over']) {
    set_human_agent_eventlisteners()
}

let width = (window.innerWidth > 0) ? window.innerWidth : screen.width;

if (width < 370) {
    document.getElementsByTagName("body")[0].innerHTML = "Your screen is to small for this game. Sorry."
}