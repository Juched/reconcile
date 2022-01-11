import {LitElement} from '../node_modules/lit-element/lit-element.js'
import {customElement} from '../node_modules/@lit/reactive-element/decorators/custom-element.js'
import {html} from '../node_modules/lit-html/lit-html.js'
import {css} from '../node_modules/@lit/reactive-element/css-tag.js'
const primary = css`#CFCCD6`;
const secondary = css`#4C6085`;
const tertiary = css`#49A078`;
const quaternary = css`#E85D75`;
const quinternary = css`#F39237`;

export class ReceiptButton extends LitElement {
  static get styles() {
    
    return css` 

    .container {
      display: flex;
      height: 100%;
    }
    .card {
      background-color: ${secondary};
      border: 2px solid ${quinternary};
      border-radius: 9px;
      margin: 5px;
      padding: 5px;
    }
    
    @import url("https://fonts.googleapis.com/css?family=Nova+Mono&display=swap");
    * {
      box-sizing: border-box;
      padding: 0;
      margin: 0;
    }

    `;
  }

  static get properties() {
    return {
      name: {type: String}
    }
  }

  constructor() {
    super();  

    
  }

  _onClick() {
    // We need to redirect to receipt page here
    // Also we can put a listner for a long press which brings up option to do a post request to delete this receipt
  }


  async firstUpdated() {
    // Give the browser a chance to paint
    await new Promise((r) => setTimeout(r, 5));

    var shadowRoot = this.shadowRoot;

    
  }
  
  

  render() {
    return html`
    <div class="card" @click="${this._onClick}">    
      ${this.name}     


    </div>`;
  }

  // VARIABLES ―――――――――――――――――――――――――
  updated(changedProperties) {
  
  
  }
}
customElements.define('receipt-button', ReceiptButton);
