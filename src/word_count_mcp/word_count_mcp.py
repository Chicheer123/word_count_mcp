import sys
import logging
from mcp.server.fastmcp import FastMCP

if sys.platform == "win32":
    sys.stderr.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("WordCounter")

app = FastMCP("WordCounter")

@app.tool()
def count_sentence_words(sentence: str) -> str:
    """统计一句话的字数。"""
    length = len(sentence)
    result = f"这句话是: {sentence}，字数: {length}"
    logger.info(f"用户输入: {sentence} | 字数统计: {length}")
    return result

def main():
    app.run(transport="stdio")  

if __name__ == "__main__":
    main()