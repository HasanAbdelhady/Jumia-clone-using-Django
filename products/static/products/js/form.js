const pobjs = document.querySelectorAll("p");
const textStyles = ["text-xl", "font-bold"];
for (p of pobjs) {
  p.classList.add("mb-2");
  p.querySelector("label").classList.add(...textStyles);
}
const in_stock = pobjs[pobjs.length - 2];
in_stock.querySelector("input").classList.remove("w-full");
const inStockStyles = ["text-green-500", "ml-3", "p-0"];
in_stock.querySelector("input").classList.add(...inStockStyles);
