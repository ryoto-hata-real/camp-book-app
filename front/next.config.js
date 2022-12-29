/** @type {import('next').NextConfig} */

const path = require("path");

const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ["cdn2.thecatapi.com"],
  },
  sassOptions: {
    includePaths: [path.join(__dirname, "styles")],
  },
  async rewrites() {
    return {
      fallback: [
        {
          source: "/:path*",
          destination: `http://localhost:8080/:path*`,
        },
      ],
    };
  },
};

module.exports = nextConfig;
