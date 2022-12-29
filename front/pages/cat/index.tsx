import { GetServerSideProps, NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import { initScriptLoader } from "next/script";
import { useState } from "react";
import styles from "../../styles/Cat.module.scss";
import "semantic-ui-css/semantic.min.scss";
import { Loader } from "semantic-ui-react";

interface SearchCatImage {
  id: string;
  url: string;
  width: number | null;
  height: number | null;
}

interface IndexPageProps {
  initialCatImageUrl: string;
}

const fetchCatImage = async (): Promise<SearchCatImage> => {
  const response_cat = await fetch(
    "https://api.thecatapi.com/v1/images/search"
  );
  const result = await response_cat.json();
  return result[0];
};

const CatHome: NextPage<IndexPageProps> = ({ initialCatImageUrl }) => {
  const [catImageUrl, setCatImageUrl] = useState(initialCatImageUrl);
  const [isLoading, setIsLoading] = useState(false);

  const handleClick = async () => {
    setIsLoading(true);
    const catImage = await fetchCatImage();
    setCatImageUrl(catImage.url);
    setIsLoading(false);
  };

  return (
    <div className={styles.container}>
      <h1>猫画像アプリ</h1>
      <div className={styles.image}>
        {isLoading ? (
          <Loader active size="huge" />
        ) : (
          <Image
            src={catImageUrl}
            alt="今日の猫さん"
            layout="fill"
            objectFit="contain"
          ></Image>
        )}
      </div>

      <button onClick={handleClick}>今日の猫さん</button>
    </div>
  );
};

export const getServerSideProps: GetServerSideProps<
  IndexPageProps
> = async () => {
  const catImage = await fetchCatImage();

  return {
    props: {
      initialCatImageUrl: catImage.url,
    },
  };
};
export default CatHome;
