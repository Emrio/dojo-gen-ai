import React, { useEffect } from "react"
import AudioReactRecorder, { RecordState } from "audio-react-recorder"
import { Streamlit } from "streamlit-component-lib"

export const App = () => {
  const [recordState, setRecordState] = React.useState<RecordState | null>(null)
  const [url, setUrl] = React.useState<string | null>(null)

  const isRecording = recordState === RecordState.START

  useEffect(() => {
    if (recordState === RecordState.START) {
      setUrl(null)
    }
  }, [recordState])

  return (
    <>
      <div>Ready to build your AI note taker ? Let's go 🚀🚀🔥</div>
      <AudioReactRecorder state={recordState} onStop={onStop} />

      <button
        onClick={() => {
          setRecordState(isRecording ? RecordState.STOP : RecordState.START)
        }}
      >
        {isRecording ? "Stop" : "Start"}
      </button>

      <br />

      {url && <audio src={url} controls />}
    </>
  )

  async function onStop({
    blob,
    url,
  }: {
    blob: Blob
    url: string
  }): Promise<void> {
    setUrl(url)

    const buffer = await blob.arrayBuffer()
    const data = new Uint8Array(buffer)

    Streamlit.setComponentValue({ arr: data })
  }
}
