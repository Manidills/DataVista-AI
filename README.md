# Decentralytics

## Overview
Decentralytics is a groundbreaking data analytics tool that leverages the power of decentralization using Filecoin/IPFS to provide efficient, cost-effective, and secure analytics solutions. With Decentralytics, users can upload their data and receive detailed analytics powered by AI models in minutes, without the need for intermediaries.

## Problem Statement
In today's data-driven world, providing robust data analytics solutions presents several challenges:
- **Storage Limitations**: Handling and storing large volumes of data is increasingly difficult and costly.
- **Complex Architectures**: Designing and maintaining complex analytics architectures requires significant expertise and resources.
- **High Server Costs**: Running data analytics on centralized servers incurs substantial costs.
- **Multiple Pipelines**: Managing various data pipelines adds to the complexity and cost.
- **Knowledgeable Personnel**: There's a high demand for skilled professionals to manage and analyze data.
- **Lack of Open-Source Solutions**: There are limited open-source platforms available for users to obtain analytics for their data without intermediaries.
- **Time-Consuming Analytics**: Obtaining analytics quickly is challenging, often requiring significant time and resources.

## Solution: Decentralytics
Decentralytics addresses these challenges by:
- **Decentralized Storage**: Utilizing Filecoin/IPFS for decentralized data storage, reducing dependency on costly centralized storage solutions.
- **Simplified Architecture**: Streamlining the analytics architecture to be more efficient and easier to manage.
- **Cost Efficiency**: Lowering server and storage costs by leveraging decentralized infrastructure.
- **Unified Pipeline**: Offering an integrated solution that minimizes the need for multiple data pipelines.
- **Accessibility**: Providing an open-source platform that democratizes access to data analytics, allowing users to obtain insights without intermediaries.
- **Quick AI-Powered Analytics**: Enabling users to upload their data and receive detailed analytics powered by AI models within minutes.

## Benefits
- **Cost Savings**: Significant reduction in storage and server costs for companies.
- **Security and Privacy**: Enhanced data security and privacy through decentralized storage.
- **Ease of Use**: Simplified deployment and management of analytics tools.
- **Open-Source**: A transparent and community-driven approach that fosters innovation and collaboration.
- **Fast Analytics**: Rapid turnaround time for obtaining analytics using AI models.

## Architecture

### Data Collection
1. **Set up Airflow DBT cron jobs**: Configure scheduled tasks for data collection using Airflow and DBT.
2. **Schedule periodic data collection**: Ensure data is collected at regular intervals.
3. **Ensure data is collected in batch-wise**: Collect data in manageable batches for efficiency.
4. **Verify data integrity**: Check the accuracy and consistency of the collected data.
5. **Clean and preprocess data**: Prepare data by cleaning and preprocessing.
6. **Store data in respective tables**: Organize the data into appropriate database tables.
7. **Use Filecoin/IPFS for storage**: Store the data securely using decentralized Filecoin/IPFS.
8. **Confirm data storage success**: Verify that data storage has been successful.

### Data Security
1. **Encrypt files using LIT protocol**: Securely encrypt data files.
2. **Encrypt CID of IPFS URL**: Encrypt the Content Identifier (CID) of the IPFS URL for added security.
3. **Store encryption keys securely**: Keep encryption keys in a secure location.

### Data Categorization
1. **Categorize encrypted CIDs**: Organize encrypted CIDs into categories.
2. **Identify data for dashboards**: Determine which data will be used for dashboards.
3. **Identify data for outsourcing**: Decide which data can be outsourced for further processing.
4. **Create categories for easy retrieval**: Set up categories to facilitate easy data retrieval.

### Data Retrieval
1. **Define data retrieval requirements**: Specify what data needs to be retrieved.
2. **List specific data needs**: Enumerate the specific data required.
3. **Determine decryption criteria**: Establish criteria for data decryption.
4. **Decrypt data using LIT protocol**: Decrypt the data using the LIT protocol.
5. **Validate data accuracy post-decryption**: Ensure the accuracy of the data after decryption.

![Alt text](https://i.postimg.cc/L66Fy4fm/untitled.png)

## Features

### Dashboards
- **Recent Hot Web3 Protocols Data**: Our dashboards serve the latest data from emerging Web3 protocols, leveraging our comprehensive architecture.
- **Core Database**: Utilizes **Lighthouse** and **Web3.storage IPFS** as the backbone for data storage.
  - **Lighthouse**: Ensures secure and efficient storage of data on a decentralized network.
  - **Web3.storage IPFS**: Provides a robust and scalable solution for data storage and retrieval.
- **Security**: Data encryption and decryption are handled using the **LIT protocol**, ensuring high levels of security and privacy.

### Analytics
- **Automated Analytics**: Users can upload CSV/XLSX files and receive detailed analytics powered by AI models.
- **User-Friendly**: Provides analytics without requiring coding knowledge or intermediaries.
- **Data Storage and Retrieval**: Utilizes services like **Web3.storage**, **Lighthouse**, **NFTPort**, **Moralis**, **Pinata**, and **Estuary** for uploading and downloading reports within our architecture.
  - **Web3.storage**: Decentralized storage for secure and efficient data handling.
  - **Lighthouse**: Decentralized storage ensure data integrity and accessibility.
  - **NFTPort, Moralis, Pinata, Estuary**: Provide additional options for data management, enhancing flexibility and user choice.

### Explorer
- **Network Details**: Provides comprehensive details for **Filecoin (Zondex)**, **WeatherXM**, and Near Network.
- **Premium Features**: Offers AI anomaly detection and prediction over time, available to premium users ( please do hold usdc token ).
  - ![Alt text](https://i.postimg.cc/B65bcBsg/Screenshot-from-2024-06-02-15-33-52-1.png)
  - **User Validation**: Utilizes the **LIT protocol signature method** to validate users. Access to premium features is granted only to users with specific tokens.
- **Decentralized Storage**: Follows the same architecture, using **IPFS CIDs** for data management and security.

## Acknowledgments

This project wouldn't have been possible without the APIs and data provideders, We are immensely grateful for their support and the resources they have made available to the developer community.

**Zondax** -

`https://api.zondax.ch/fil/data/v3/mainnet/transactions/erc20/address/{address}/transfers`
`https://api.zondax.ch/fil/data/v3/mainnet/transactions/erc20/contract/{contract_address}/address/{address}/transfers`
`https://api.zondax.ch/fil/data/v3/mainnet/stats/gas-used/{FIL_address}/monthly?sort_by=bucket:desc`
`https://api.zondax.ch/fil/data/v3/mainnet/stats/gas-used/{FIL_address}/monthly/cumulative?sort_by=bucket:desc"`
`https://api.zondax.ch/fil/data/v3/mainnet/stats/value-exchanged/{FIL_address}/latest?data_points=10`
`https://api.zondax.ch/fil/data/v3/mainnet/stats/value-exchanged/{FIL_address}/latest/cumulative`
`https://api.zondax.ch/fil/data/v3/mainnet/erc20/contracts?sort=holders&order=desc`
`https://api.zondax.ch/fil/data/v3/mainnet/stats/rich-list/10?sort_by=bucket:asc`
`https://api.zondax.ch/fil/data/v3/mainnet/stats/contract/global/create/monthly?sort_by=bucket:asc`
`https://api.zondax.ch/fil/data/v3/mainnet/stats/contract/global/create/monthly/cumulative?sort_by=bucket:desc`
`https://api.zondax.ch/fil/data/v3/mainnet/stats/contract/top/unique-users?limit=10`
`https://api.zondax.ch/fil/data/v3/mainnet/stats/gas-used/top/accounts?limit=10`

**WeatherXM**

`https://api.weatherxm.com/api/v1/cells/{area_index}/devices`
`https://api.weatherxm.com/api/v1/cells`
`https://api.weatherxm.com/api/v1/network/search?query={area}&exact=true`
`https://api.weatherxm.com/api/v1/network/stats`
`https://api.weatherxm.com/api/v1/network/stats/supply/total`
`https://api.weatherxm.com/api/v1/network/stats/supply/circulating`

**LIT Protocol**

`https://github.com/LIT-Protocol/js-sdk`

`https://github.com/AlgoveraAI/streamlit-metamask`


**Lighthouse**
` https://docs.lighthouse.storage`

**Pinata**
`https://github.com/PinataCloud/Pinata-SDK`

**Web3storage**
` https://web3.storage/docs`

**Moralis**
` https://moralis.io/how-to-upload-files-to-ipfs-full-guide`

**Nftport**
`https://docs.nftport.xyz/reference/upload-file-to-ipfs`

**Estuary**
` https://docs.estuary.tech`

## Why Decentralytics is the Need of the Hour

### Transforming the Analytics Domain

Decentralytics is set to revolutionize the data analytics domain by addressing several critical challenges and making advanced analytics accessible to a broader audience. Here's how it helps people and makes a significant impact:

### Democratizing Data Analytics
- **Accessibility**: Decentralytics eliminates the need for intermediaries, making it easy for anyone to obtain detailed data analytics without requiring extensive coding knowledge.
- **Cost-Effective**: By leveraging decentralized storage solutions like Filecoin/IPFS, it significantly reduces storage and server costs, making data analytics affordable for small businesses and individuals.

### Enhancing Data Security and Privacy
- **Secure Storage**: Utilizing **Lighthouse** and **Web3.storage IPFS** ensures that data is stored securely in a decentralized manner.
- **Data Encryption**: The use of the **LIT protocol** for encryption and decryption safeguards user data, maintaining high levels of privacy and security.

### Providing Rapid and Detailed Insights
- **AI-Powered Analytics**: Users can upload their data in CSV/XLSX formats and receive comprehensive analytics reports generated by AI models within minutes. This helps users quickly gain insights and make informed decisions.
- **User-Friendly Dashboards**: The dashboards offer real-time data from the latest Web3 protocols, helping users stay updated with minimal effort.

### Empowering Users with Premium Features
- **Advanced Network Insights**: The Explorer feature provides detailed insights into networks like Filecoin, WeatherXM, and Near Network. Premium features include AI anomaly detection and predictions, offering advanced analytics capabilities.
- **Token-Based Access**: Premium features are accessible through token validation using the **LIT protocol signature method**, ensuring secure and exclusive access to advanced tools.

### Making a Difference for Common People
Decentralytics brings the power of advanced data analytics to the masses, allowing small businesses, researchers, and individual users to harness the potential of their data without significant financial or technical barriers. By democratizing access to data analytics and ensuring security and privacy, Decentralytics is poised to make a substantial impact in the analytics domain.



## License
Decentralytics is licensed under the MIT License. See the [LICENSE](https://github.com/YourUsername/Decentralytics/blob/main/LICENSE) file for more information.

---

