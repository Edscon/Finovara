import{a as e,f as t}from"./core-Dwn9Kajy.js";const{get:r}=Reflect,a=["preventDefault","stopPropagation","stopImmediatePropagation"],n={once:!0};class o{#e;constructor(e){this.#e=e}get(e,t){return"currentTarget"===t?this.#e:((e,t)=>"function"==typeof t?t.bind(e):t)(e,r(e,t))}}const{stringify:s}=JSON,c=(e,t)=>`${e}(code, ${t.join(", ")})`,i=({type:e="py",persistent:r,terminal:i,config:l})=>{const _=r?["globals()","__locals__"]:["{}","{}"],u=URL.createObjectURL(new Blob([["from pyscript import sync, config",'__message__ = lambda e,v: f"[31m[1m{e.__name__}[0m: {v}"',"__locals__ = {}",'if config["type"] == "py":',"\timport sys","\tdef __error__(_):","\t\tinfo = sys.exc_info()","\t\treturn __message__(info[0], info[1])","else:","\t__error__ = lambda e: __message__(e.__class__, e.value)","def execute(code):",`\ttry: return ${c("exec",_)};`,"\texcept Exception as e: print(__error__(e));","def evaluate(code):",`\ttry: return ${c("eval",_)};`,"\texcept Exception as e: print(__error__(e));","sync.execute = execute","sync.evaluate = evaluate"].join("\n")])),p=t(document.createElement("script"),{type:e,src:u});return p.toggleAttribute("worker",!0),p.toggleAttribute("terminal",!0),i&&p.setAttribute("target",i),l&&p.setAttribute("config","string"==typeof l?l:s(l)),((e,t,r=null)=>new Promise(((s,c)=>{const i=new o(e);if(r.signal){const e=e=>c(new Proxy(e,i));if(r.signal.addEventListener("abort",e,n),r.signal.aborted)return r.signal.dispatchEvent(new Event("abort"))}e.addEventListener(t,(e=>{for(const t of a)r[t]&&e[t]();s(new Proxy(e,i))}),{...r,...n})})))(document.body.appendChild(p),`${e}:done`,{stopPropagation:!0}).then((()=>(URL.revokeObjectURL(u),p)))},l=async e=>{const t=await i(e),{xworker:r,process:a,terminal:n}=t,{execute:o,evaluate:s}=r.sync;return t.remove(),{xworker:r,process:a,terminal:n,execute:o,evaluate:s}};var _=async(t={})=>{let r=await l(t),a=!1;const n=()=>{r&&(r.xworker.terminate(),r.terminal.dispose(),r=null),a=!1},o=async()=>{n(),r=await l(t)},s=t=>async n=>{a&&await o(),a=!0;try{return await r[t](e(n))}catch(e){console.error(e)}finally{a=!1}},c=e=>async()=>{a?await o():r?.terminal[e]()};return{process:s("process"),execute:s("execute"),evaluate:s("evaluate"),clear:c("clear"),reset:c("reset"),kill:n}};export{_ as default};
//# sourceMappingURL=donkey-Kizedq97.js.map
