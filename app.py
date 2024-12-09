from flask import Flask, request, jsonify
from environs import Env

from helpers import validate_time_format

from get_prices import get_prices_from_binance


env = Env()
env.read_env()


DEBUG = env.bool("DEBUG")


app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_data():

    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")

    # Проверяем наличие обязательных параметров
    if not start_time or not end_time:
        return jsonify({"error": "start_time and end_time are required"})

    # Проверяем формат времени
    if not validate_time_format(start_time):
        return jsonify({"error": f"Invalid start_time format. Expected format: 'YYYY-MM-DDTHH:MM:SS'"})
    if not validate_time_format(end_time):
        return jsonify({"error": f"Invalid end_time format. Expected format: 'YYYY-MM-DDTHH:MM:SS'"})

    params = {
        "start_time": request.args.get("start_time"),
        "end_time": request.args.get("end_time"),
        "symbol": request.args.get("symbol", "ETHUSDT"),
        "interval": request.args.get("interval", "1m"),
        "limit": request.args.get("limit", "1000"),
    }

    prices = get_prices_from_binance(params)
    if prices is None:
        return jsonify({"param": "no prices"})
    
    response = {"param": prices}
    
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=DEBUG)