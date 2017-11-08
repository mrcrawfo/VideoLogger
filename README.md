# VideoLogger

This is a tool intended for gamedev use: in order to learn more about existing games in the market, I believe it might be useful to datamine video longplays. The intent for my own use case would be to gather information on playtime of each chapter of a game, battle frequency and average duration, cutscene length, etc.

Since my target genre in particular is made up of games which may last 40 hours or more, it is important to make the logging process as streamlined as possible. Having an embedded player should remove the extra clicks to navigate or shift focus between multiple tabs, as well as hopefully making the timestamps of a given video accessible in real-time. The rest of the UI should be designed to encode these markers to a given category without ever needing to pause playback, either through a bar of buttons or keyboard input.

These categories should be editable, although there may be presets suited to different genre needs. For the example of a JRPG, the default should probably be something like:
1. Cutscene
2. Menu
3. Walk Screen
4. Battle Screen
 
Pressing any of those numeric keys or buttons would create a record of that category of play at the associated timestamp, segmenting the runtime of the video into these categories by connecting each point to the next. The UI should also allow manual insert/edit/delete of any of these pieces of data, as well as a basic timeline viewer color-coded to show the general proportion of these categories at a glance. Although this may not apply to every game type, the +/- keys should adjust the current chapter or level in which events are occurring, to allow clearer coordination of data across multiple videos.

Data storage will likely be done using the [local storage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API) of the browser itself, segregated by video with a unique key likely taken from the provided URL. Though some analytics should be possible within the page itself, it will likely be more useful to provide a batch export feature to output to text files which can be crawled and aggregated by an external script. Any such tools for parsing the resulting data can eventually be included in this repository as well.

If this proves to be a useful tool for my own development work then I would like to look into open-sourcing it and making it a tool for others to use as well.
