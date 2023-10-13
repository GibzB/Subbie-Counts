// Sample channel data, you can add more channels
const channels = [
    // Andrew Kibe Subscribers
    { url: "https://mixerno.space/embed/youtube-channel-counter/UCl6ICaB9meBcSMQ5Zmr446g?counter=0" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCMD-JmezXoQiV9PiWLwVpGQ" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCBZPPYU_l99Mg6-GXm6xbMg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    { name: "Channel 1", url: "https://mixerno.space/embed/youtube-channel-counter/UCiXj0BfxM0WQGFr9mxdR0qg" },
    // Andrew Kibe Subscribers
    

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
