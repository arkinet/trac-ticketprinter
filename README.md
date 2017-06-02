# trac-ticketprinter
A plugin for trac that creates a printable html page of tickets to use on a scrum board

## Usage
After installing the plugin a new link should be added at the bottom of the query page with the name "Ticket printer".
This will save a html-file, open that in your browser and print it in landscape mode.

## Installation
1. Clone/Download this repository
2. Run `python setup.py bdist_egg`
3. Upload dist/TracTicketPrinter-*.egg in trac admin
