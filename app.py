from flask import Flask, request, jsonify

from get_prices import get_prices_from_binance


app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_data():

    params = {
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
    app.run(debug=True)