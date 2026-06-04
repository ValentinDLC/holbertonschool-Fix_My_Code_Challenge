#!/usr/bin/node
if (process.argv.length <= 2) {
    process.stderr.write("Usage: ./1-print_square.js <size>\n");
    process.exit(1);
}

const size = parseInt(process.argv[2], 10);
const row = "#".repeat(size) + "\n";
process.stdout.write(row.repeat(size));
