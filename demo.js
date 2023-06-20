/* eslint-disable no-console */
import { LightningElement, track } from 'lwc';  // eslint-disable-line no-unused-vars

function calculateDaysToChristmas() {
    const now = new Date();
    const christmas = new Date(now.getFullYear(), 11, 25);
    if (now.getMonth() === 11 && now.getDate() > 25) {
        christmas.setFullYear(christmas.getFullYear() + 1);
    }
    const difference = christmas.getTime() - now.getTime();
    return Math.ceil(difference / (1000 * 60 * 60 * 24));
}

// eslint-disable-next-line no-unused-vars
function process() {
    const daysToChristmas = calculateDaysToChristmas();   
    console.log(`Days to Christmas: ${daysToChristmas}`);
}




