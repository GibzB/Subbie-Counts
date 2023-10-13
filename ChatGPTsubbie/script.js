// Sample channel data, you can add more channels
const channels = [
    // Channel_TukoKenya Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UCl6ICaB9meBcSMQ5Zmr446g?counter=0" },
    // Channel_EveMungai Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UCcBNWxvAXH-nTAzOeuuLHgw" },
    // Channel_PresenterAli Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UCMD-JmezXoQiV9PiWLwVpGQ" },
    // Channel_CrazyKennar Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Channel_SautiSol Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UCBZPPYU_l99Mg6-GXm6xbMg" },
    // Channel_Bahati Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UC2O6vD7gjgZIXKVegD6qOHA" },
    // Channel_Wajesus Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UCHVTpHXp43Giiwag5s6o8xQ" },
    // Channel_DianaB Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UC0UslOx9EYxnk_4SFSHj8hA" },
    // Channel_WillyPaul Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UCgdVgtJQXxebSiSAzlhYczw" },
    // Channel_KhaligraphJones Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UCRRSCAz5VJQqJHAIPgFVCxw" },
    // Channel_Desagu Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UC7MGnWilDcg157op0eKI1Tg?counter=0" },
    // Channel_Njugush Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UCkV3t4uxBsi8jYj3wjqooeQ?counter=0" },
    // Channel_AbelMutua Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UC4tjY2tTltEKePusozUxtSA" },
    // Channel_LynnNgugi Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UCa2gldA2ivhzMwIJRA5683w?counter=0" },
    
    
    // Add more channels here
];

const table = document.getElementById("channel-table");

channels.forEach(channel => {
    const channelCard = document.createElement("div");
    channelCard.classList.add("channel-card");

    const iframe = document.createElement("iframe");
    iframe.src = channel.url;
    iframe.width = "410";
    iframe.height = "120";

    channelCard.appendChild(iframe);

    const channelTitle = document.createElement("div");
    channelTitle.classList.add("channel-title");
    channelTitle.textContent = channel.name;

    channelCard.appendChild(channelTitle);

    const channelSubscribers = document.createElement("div");
    channelSubscribers.classList.add("channel-subscribers");
    channelCard.appendChild(channelSubscribers);

    table.appendChild(channelCard);
});
